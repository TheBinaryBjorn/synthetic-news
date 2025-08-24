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

class TopicException(Exception):
    """
    This class is an exception raised by the service manager.
    """
    def __init__(self, message="Topic not allowed."):
        self.message=message
