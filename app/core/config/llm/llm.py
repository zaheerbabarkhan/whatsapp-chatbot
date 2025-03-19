from langchain_groq import ChatGroq

from app.core.config.config import settings

class LLMService:
    def __init__(self):
        self.llm = ChatGroq(
                model=settings.GROQ_MODEL_NAME,
                temperature=0.0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                api_key=settings.GROQ_API_KEY,
            )