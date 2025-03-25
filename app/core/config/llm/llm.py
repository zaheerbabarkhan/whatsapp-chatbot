import logging

from llama_index.llms.groq import Groq
from app.core.config.config import settings
from app.exceptions.llm import LLMInitException

logger = logging.getLogger(__name__)

def get_groq():
    
    try:
        groq = Groq(
        model=settings.GROQ_MODEL_NAME,
        api_key=settings.GROQ_API_KEY,
    )
        yield groq
    except Exception as e:
        logger.exception("Error initializing Groq LLM %s",e)
        raise LLMInitException(str(e)) from e
        pass