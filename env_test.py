from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
print("ENV FILE EXISTS:", env_path.exists())

load_dotenv(dotenv_path=env_path)
print("RAW VALUE:", repr(os.getenv("WEATHERSTACK_API_KEY")))
