import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Global embeddings client
emb_client = OpenAI(api_key=OPENAI_API_KEY)

def get_llm(
    model_name: str = "gpt-4.1-mini-2025-04-14",
    temperature: float = 0.3,
    max_tokens: int = 512
):
    return ChatOpenAI(
        model_name=model_name,
        openai_api_key=OPENAI_API_KEY,
        temperature=temperature,
        max_tokens=max_tokens
    )

# ✅ Global default LLM (import this everywhere)
llm = get_llm()