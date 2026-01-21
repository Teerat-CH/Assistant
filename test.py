import time
from RAG import RAG

start = time.time()
rag_system = RAG(load_from_file=True)
print(f"Load RAG from file: {time.time() - start:.3f}s")
print(f"Documents loaded: {len(rag_system.index.documents)}")

start = time.time()
result = rag_system.query("what is my name")
print(f"Query 1: {time.time() - start:.3f}s")
print(result)