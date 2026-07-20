from modules.rag import load_pdf
from modules.rag import create_vector_db


chunks = load_pdf(
    "data/uploads/customer_sales.pdf"
)

db = create_vector_db(chunks)

print("Vector Database Created Successfully")