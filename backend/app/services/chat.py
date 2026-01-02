from typing import AsyncGenerator, List, Dict, Any
from openai import AsyncOpenAI
from .openai_client import get_client


async def stream_completion(
    messages: List[Dict[str, str]],
    model: str = "gpt-4",
    temperature: float = 0.7,
) -> AsyncGenerator[str, None]:
    """Stream chat completion tokens."""
    client = await get_client()

    stream = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True,
    )

    async for chunk in stream:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


async def complete(
    messages: List[Dict[str, str]],
    model: str = "gpt-4",
) -> Dict[str, Any]:
    """Non-streaming completion."""
    client = await get_client()

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return {
        "content": response.choices[0].message.content,
        "tokens": response.usage.total_tokens,
    }
