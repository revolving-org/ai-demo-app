import os
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).parent
CONFIG_DIR = ROOT_DIR / "config"

# App settings
APP_NAME = "AI Demo API"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
