"""
This module is in charge of sending messages to an LLM model.
"""
import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from google import genai

class LlmService(ABC):
    """
    Abstract class for all LLM Services.
    """
    @abstractmethod
    def send_message_to_llm(self,text: str) -> str:
        pass

class GeminiService(LlmService):
    """
    An LlmService that utilizes Gemini API for LLM communication.
    """
    def __init__(self):
        """
        Initializes the Service with the Gemini API key.
        """
        load_dotenv()
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=gemini_api_key)
        self.model = 'gemini-2.5-flash'

    def send_message_to_llm(self,text):
        """
        Sends a given text to the LLM model.
        """
        response = self.client.models.generate_content(model=self.model,contents=text)
        return response.text
