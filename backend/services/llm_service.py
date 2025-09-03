"""
This module is in charge of sending messages to an LLM model.
"""

from abc import ABC, abstractmethod

from google import genai

from .exceptions import LlmMessageException


class LlmService(ABC):
    """
    Abstract class for all LLM Services.
    """

    @abstractmethod
    def send_message_to_llm(self, text: str) -> str:
        pass


class GeminiService(LlmService):
    """
    An LlmService that utilizes Gemini API for LLM communication.
    """

    ALLOWED_MODELS = ["gemini-2.5-flash"]

    def __init__(self, client: genai.Client, model: str = "gemini-2.5-flash"):
        """
        Initializes the Service with the Gemini API key.
        """
        if not isinstance(client, genai.Client):
            raise TypeError
        if not isinstance(model, str):
            raise TypeError
        if not model or not model.strip():
            raise ValueError
        if model not in self.ALLOWED_MODELS:
            raise ValueError
        self.client = client
        self.model = model

    def send_message_to_llm(self, text: str) -> str:
        """
        Sends a given text to the LLM model.
        """
        if not isinstance(text, str):
            raise TypeError
        if text == "" or text.strip() == "":
            raise ValueError

        try:
            response = self.client.models.generate_content(
                model=self.model, contents=text
            )
        except Exception as e:
            raise LlmMessageException("LLM Model Failed.") from e

        try:
            return_text = response.text
        except Exception as e:
            raise LlmMessageException("Failed to extract response.") from e

        if not return_text:
            raise LlmMessageException("Error: Empty LLM response.")

        return response.text
