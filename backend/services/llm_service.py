from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os
from google import genai

class LLM_Service(ABC):
    @abstractmethod
    def send_message_to_llm(text: str) -> str:
        pass

class GeminiService(LLM_Service):
    def __init__(self):
        load_dotenv()
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = 'gemini-2.5-flash'

    def send_message_to_llm(self,text):
        response = self.client.models.generate_content(model=self.model,contents=text)
        return response.text
