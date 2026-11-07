import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().with_name(".env"))

required_settings = {
    "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "AZURE_OPENAI_DEPLOYMENT": os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    "AZURE_OPENAI_API_KEY": os.getenv("AZURE_OPENAI_API_KEY"),
}
missing_settings = [name for name, value in required_settings.items() if not value]

if missing_settings:
    missing = ", ".join(missing_settings)
    raise RuntimeError(
        f"Missing required environment variables: {missing}. "
        "Set them in .env or your environment."
    )

client = OpenAI(
    base_url=required_settings["AZURE_OPENAI_ENDPOINT"],
    api_key=required_settings["AZURE_OPENAI_API_KEY"],
)
deployment_name = required_settings["AZURE_OPENAI_DEPLOYMENT"]