"""Application settings loaded from environment variables."""

from __future__ import annotations

from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── App ──────────────────────────────────────────────────
    environment: str = "development"
    auto_create_tables: bool = True

    # ── Database ─────────────────────────────────────────────
    database_url: str = "sqlite:///./pathly.db"

    # ── CORS ─────────────────────────────────────────────────
    cors_origins: str = "http://localhost:3000,http://localhost:5173,http://localhost:8000"

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _parse_cors_origins(cls, v):
        if isinstance(v, str):
            return v
        if isinstance(v, list):
            return ",".join(v)
        return str(v)

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    # ── JWT Auth ─────────────────────────────────────────────
    jwt_secret_key: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"

    # ── NVIDIA NIM (curriculum generation) ───────────────────
    nvidia_api_key: str = ""
    nvidia_model: str = "openai/gpt-oss-120b"
    nvidia_base_url: str = "https://integrate.api.nvidia.com/v1"

    # ── OpenRouter (AI explanations) ─────────────────────────
    openrouter_api_key: str = ""
    openrouter_model: str = "nvidia/nemotron-3.5-lightning:free"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"

    # ── YouTube ──────────────────────────────────────────────
    youtube_api_key: str = ""

    # ── Qdrant (vector search) ──────────────────────────────
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333

    # ── Redis (leaderboard) ─────────────────────────────────
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
