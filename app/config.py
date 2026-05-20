from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fraud Review Assistant"
    openai_api_key: str | None = None
    pinecone_api_key: str | None = None
    pinecone_index_name: str = "fraud-review-assistant"
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o-mini"
    use_pinecone: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
