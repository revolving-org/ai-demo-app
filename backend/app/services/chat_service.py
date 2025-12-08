from typing import List, Dict, Any, AsyncGenerator
from dataclasses import dataclass
from .chat import stream_completion, complete
from .embeddings import create_embedding


@dataclass
class ChatMessage:
    role: str
    content: str


class ChatService:
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.system_prompt: str | None = None

    def set_system_prompt(self, prompt: str) -> None:
        self.system_prompt = prompt

    def _build_messages(
        self, messages: List[ChatMessage]
    ) -> List[Dict[str, str]]:
        result = []
        if self.system_prompt:
            result.append({"role": "system", "content": self.system_prompt})
        result.extend([{"role": m.role, "content": m.content} for m in messages])
        return result

    async def respond(
        self, messages: List[ChatMessage]
    ) -> Dict[str, Any]:
        formatted = self._build_messages(messages)
        return await complete(formatted, model=self.model)

    async def stream(
        self, messages: List[ChatMessage]
    ) -> AsyncGenerator[str, None]:
        formatted = self._build_messages(messages)
        async for token in stream_completion(formatted, model=self.model):
            yield token

    async def embed(self, text: str) -> List[float]:
        return await create_embedding(text)
