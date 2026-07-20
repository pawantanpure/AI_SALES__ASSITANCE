from modules.rag import load_vector_db

db = load_vector_db()

docs = db.similarity_search(
    "What is relationship selling?",
    k=3
)

for doc in docs:
    print(doc.page_content)
    print("-"*50)