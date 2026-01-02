from typing import List
from .openai_client import get_client


async def create_embedding(text: str) -> List[float]:
    """Generate embedding vector for text."""
    client = await get_client()

    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        encoding_format="float",
    )

    return response.data[0].embedding


async def create_embeddings_batch(
    texts: List[str],
    batch_size: int = 100,
) -> List[List[float]]:
    """Generate embeddings for multiple texts."""
    client = await get_client()
    embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = await client.embeddings.create(
            model="text-embedding-3-small",
            input=batch,
        )
        embeddings.extend([d.embedding for d in response.data])

    return embeddings
