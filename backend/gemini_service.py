import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables once at the start of the script
load_dotenv()

class GeminiService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def summarize_text(self, text_to_summarize):
        prompt = f"""Please summarize the following TLDR Newsletter mail. Format the summary as a script for a podcaster, using clear, 
        conversational language. Avoid using any markdown formatting, special characters, or emojis. 
        The output should be a single block of plain text, ready to be read aloud. 
        The tone should be friendly and engaging, 
        as if you're speaking directly to a listener.
        Here is the text to summarize:\n\n{text_to_summarize}"""
        
        response = self.model.generate_content(prompt)
        return response.text