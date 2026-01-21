from fastapi import FastAPI

app = FastAPI()

@app.get("/wakeup")
def wakeup():
	return {"message": "service waking up!"}
	
@app.post("/query")
def generate_response(text: str):
	text = text + "!"
	return {"response": text}