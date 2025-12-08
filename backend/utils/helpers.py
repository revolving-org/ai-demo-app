import re
from typing import Any
from datetime import datetime


def normalize_text(text: str) -> str:
    """Normalize text for processing."""
    return " ".join(text.strip().lower().split())


def truncate(text: str, max_length: int = 100) -> str:
    """Truncate text with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def sanitize_filename(name: str) -> str:
    """Remove invalid filename characters."""
    return re.sub(r'[<>:"/\\|?*]', "_", name)
