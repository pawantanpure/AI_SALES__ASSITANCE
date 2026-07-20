from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import Ollama

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks

def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


def create_vector_db(chunks):

    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return db


def load_vector_db():

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    return db


def get_llm():

    llm = Ollama(
        model="llama3"
    )

    return llm



def ask_question(question):

    db = load_vector_db()

    docs = db.similarity_search(
        question,
        k=4
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer only from the context.

    Context:
    {context}

    Question:
    {question}
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    return response