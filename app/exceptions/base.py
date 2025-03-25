class BaseAppException(Exception):
    """
    A base exception class for the application.
    All custom exceptions should inherit from this class.
    """
    def __init__(self, message=None):
        if message is None:
            message = "An error occurred while processing your request. Please contact the administrator."
        super().__init__(message)