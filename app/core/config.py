from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "RAG Chat"
    DEBUG: bool = False

    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384

    CHROMA_PERSIST_DIR: str = "./chroma_db"
    CHROMA_COLLECTION: str = "documents"

    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 64

    TOP_K_RESULTS: int = 5     
    MEMORY_WINDOW: int = 6      

    LLM_MODEL: str = "gpt-4.1-mini"
    AZURE_OPENAI_API_KEY: Optional[str] = None
    AZURE_OPENAI_ENDPOINT: Optional[str] = None
    AZURE_OPENAI_DEPLOYMENT: Optional[str] = None
    AZURE_OPENAI_API_VERSION: str = "2025-01-01-preview"

    TOKEN_LOG_FILE: str = "./logs/token_usage.jsonl"

    class Config:
        env_file = ".env"


settings = Settings()