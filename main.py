from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from collections import deque
from RAG import RAG
import requests
import os
from dotenv import load_dotenv

# load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your domain: ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_histories: dict[str, deque] = {}

try:
    rag_system = RAG(load_from_file=True)
except FileNotFoundError:
    rag_system = None
    print("Warning: Index files not found. Run build_index.py first.")

@app.get("/wakeup")
def wakeup():
	return {"message": "service waking up!"}
	
@app.post("/query")
def query(query: str, session_id: str = "default"):
    if rag_system is None:
        raise HTTPException(status_code=503, detail="RAG system not initialized. Index files missing.")
    try:
        if session_id not in user_histories:
            user_histories[session_id] = deque(maxlen=7)
        history = user_histories[session_id]
        
        if history:
            history_context = "\n".join([f"- {q}" for q in history])
            query_with_context = f"Previous questions:\n{history_context}\n\nCurrent question: {query}"
        else:
            query_with_context = query
        
        result = rag_system.query(query_with_context)
        
        history.append(query)

        requests.post(
            DISCORD_WEBHOOK_URL,
            json={"content": f"Session_ID: {session_id}\nUser query: {query}\nAI response: {result}"}
        )
        
        return {"response": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generate response failed: {str(e)}")

@app.delete("/history")
def clear_history(session_id: str = "default"):
    if session_id in user_histories:
        user_histories[session_id].clear()
    return {"message": "History cleared"}