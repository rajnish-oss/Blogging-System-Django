import chromadb
from chromadb.config import Settings
from pydantic import BaseModel



class vector_db(BaseModel):
    id: str
    content: str
    source: str

def create_vector_db(data: vector_db):
    chroma_client = chromadb.EphemeralClient(Settings(persist_directory="./chroma_db/"))

    collection = chroma_client.get_or_create_collection(name="my_collection")

    words = data.content.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + 100
        chunks.append(' '.join(words[start:end]))
        start += 100 - 50

    ids = [f"{data.id}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": data.source} for _ in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=metadatas
    )



def get_context(query: str):
    chroma_client = chromadb.EphemeralClient(Settings(persist_directory="./chroma_db/"))
    try:
        collection = chroma_client.get_collection(name="my_collection")
    except Exception as e:
        # Return None if the collection is not found
        print(e)
        return None

    results = collection.query(
    query_texts=["This is a query document about hawaii"],
    n_results=2
    )

    return results


