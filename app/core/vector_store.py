import chromadb
from chromadb.config import Settings as ChromaSettings
from app.core.config import settings
from functools import lru_cache
from typing import Optional


@lru_cache(maxsize=1)
def get_chroma_client():
    return chromadb.PersistentClient(
        path=settings.CHROMA_PERSIST_DIR,
        settings=ChromaSettings(anonymized_telemetry=False)
    )


def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(
        name=settings.CHROMA_COLLECTION,
        metadata={"hnsw:space": "cosine"} 
    )


def upsert_chunks(chunks, embeddings: list, ids: list[str]):
    collection = get_collection()
    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        documents=[c.text for c in chunks],
        metadatas=[c.metadata for c in chunks]
    )


def query_similar(embedding: list, n_results: int = settings.TOP_K_RESULTS, where: Optional[dict] = None) -> dict:
    collection = get_collection()

    print(f"[vector_search] top_k={n_results} filter={where}")

    kwargs = {
        "query_embeddings": [embedding],
        "n_results": n_results,
        "include": ["documents", "metadatas", "distances"]
    }
    if where:
        kwargs["where"] = where
    return collection.query(**kwargs)


def delete_by_doc_id(doc_id: str):
    collection = get_collection()
    collection.delete(where={"doc_id": doc_id})