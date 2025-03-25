from .base import BaseAppException

class LLMInitException(BaseAppException):
    """
    Exception raised when there is an issue initializing an LLM.
    """
    def __init__(self, message=None):
        if message is None:
            message = "An error occurred while initializing the LLM. Please try again."
        super().__init__(message)