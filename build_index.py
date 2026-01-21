# Run this script once to build and save the index before deployment
from RAG import RAG

rag_system = RAG()

sample_documents = [
    "The capital of France is Paris.",
    "The largest planet in our solar system is Jupiter.",
    "The Great Wall of China is visible from space.",
    "The human body has 206 bones.",
    "The speed of light is approximately 299,792 kilometers per second.",
    "My name is John Doe"
]

print(f"Adding {len(sample_documents)} documents...")
for i, doc in enumerate(sample_documents):
    rag_system.add_document(doc)
    print(f"  Added doc {i+1}: {doc[:50]}...")

rag_system.save_index()
print("Done! Index is ready for deployment.")
