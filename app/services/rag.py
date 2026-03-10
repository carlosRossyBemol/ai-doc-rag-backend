from app.core.embeddings import embed_text
from app.core.vector_store import search

def ask_question(question):

    query_embedding = embed_text([question])[0]

    results = search(query_embedding)

    docs = results["documents"][0]

    context = "\n".join(docs)

    return context