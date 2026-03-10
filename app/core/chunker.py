from typing import List
from dataclasses import dataclass
from app.core.config import settings

@dataclass
class Chunk:
    text: str
    metadata: dict

def chunk_text(text: str, filename: str, doc_id: str) -> List[Chunk]:
    words = text.split()
    chunks = []
    chunk_size = settings.CHUNK_SIZE
    overlap = settings.CHUNK_OVERLAP
    step = chunk_size - overlap

    for i, start in enumerate(range(0, len(words), step)):
        chunk_words = words[start:start + chunk_size]

        if len(chunk_words) < 20:
            continue

        chunks.append(Chunk(
            text=" ".join(chunk_words),
            metadata={
                "doc_id": doc_id,
                "filename": filename,
                "chunk_index": i,
                "start_word": start,
                "word_count": len(chunk_words),
            }
        ))

    return chunks