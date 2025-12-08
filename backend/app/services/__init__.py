from functools import lru_cache
from .chat_service import ChatService, ChatMessage
from .embeddings import create_embedding, create_embeddings_batch


@lru_cache()
def get_chat_service() -> ChatService:
    """Get singleton chat service instance."""
    return ChatService(model="gpt-4")


__all__ = [
    "ChatService",
    "ChatMessage",
    "get_chat_service",
    "create_embedding",
    "create_embeddings_batch",
]
