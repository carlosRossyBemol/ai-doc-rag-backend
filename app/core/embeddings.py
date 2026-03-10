from sentence_transformers import SentenceTransformer
from app.core.config import settings
from functools import lru_cache
from typing import List


@lru_cache(maxsize=1)
def get_embedding_model() -> SentenceTransformer:
    print(f"[embeddings] Loading model: {settings.EMBEDDING_MODEL}")
    return SentenceTransformer(settings.EMBEDDING_MODEL)


def embed_texts(texts: List[str]) -> List[List[float]]:
    model = get_embedding_model()
    print(f"[embeddings] encoding {len(texts)} texts")
    
    embeddings = model.encode(
        texts,
        show_progress_bar=False,
        normalize_embeddings=True,  
        batch_size=32
    )
    return embeddings.tolist()


def embed_query(query: str) -> list[float]:
    return embed_texts([query])[0]