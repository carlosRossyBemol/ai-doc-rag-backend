import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(name="docs")

def add_documents(chunks, embeddings, metadata):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata,
        ids=ids
    )

def search(query_embedding):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results