from pypdf import PdfReader
from app.core.chunker import chunk_text
from app.core.embeddings import embed_text
from app.core.vector_store import add_documents

def ingest_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    print("TEXT LENGTH:", len(text))

    chunks = chunk_text(text)

    print("CHUNKS:", len(chunks))

    embeddings = embed_text(chunks)

    print("EMBEDDINGS:", len(embeddings))

    metadata = [{"source": file_path}] * len(chunks)

    add_documents(chunks, embeddings, metadata)

    print("DOCUMENT INDEXED:", file_path)