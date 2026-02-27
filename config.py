import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "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")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
