import os
import shutil
from fastapi import APIRouter, UploadFile
from app.services.ingestion import ingest_pdf

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile):

    os.makedirs("data", exist_ok=True)

    path = f"data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(path)

    return {
        "status": "uploaded",
        "filename": file.filename
    }