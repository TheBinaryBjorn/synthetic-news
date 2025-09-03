"""
This Module supplies the program with various
types of exceptions.
"""


class ResearchException(Exception):
    """
    This Class is an exception raised at the Research Service.
    """


class ScriptWriterException(Exception):
    """
    This Class is an exception raised by the Script Writer
    Service.
    """


class TtsException(Exception):
    """
    This Class is an exception raised by the TTS Service.
    """


class LlmException(Exception):
    """
    This class is an exception raised by the LLM Service.
    """


class LlmMessageException(Exception):
    """
    This class is an exception raised when sending a message
    to the selected LLM api fails.
    """


class ApiKeyException(Exception):
    """
    This class is an exception raised when there is trouble
    with any API key.
    """


class DateTimeException(Exception):
    """
    This class is an exception raised when datetime library
    functions fail.
    """


class TavilyException(Exception):
    """
    This calss is an exception raised when Tavily fails to
    do it's job.
    """


class TopicException(Exception):
    """
    This class is an exception raised by the service manager.
    """

    def __init__(self, message="Topic not allowed."):
        self.message = message
