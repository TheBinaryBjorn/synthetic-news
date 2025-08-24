"""
This module is in charge of creating podcast scripts from given
summaries.
"""
import os
from abc import ABC,abstractmethod
from datetime import datetime
from .llm_service import LLM_Service

class ScriptWriterService(ABC):
    """
    An abstract class used as an interface.
    """
    @abstractmethod
    def generate_podcast_script(self,topic, research_text):
        pass

class GeminiWriterService(ScriptWriterService):
    """
    A script writer class that uses gemini as it's LLM.
    """
    def __init__(self,llm_service: LLM_Service):
        """
        Initializes the Class with an LLM service.
        """
        self.llm_service = llm_service

    def generate_podcast_script(self, topic, research_text):
        """
        Generates a podcast script as a string from given topic and research summary.
        """
        try:
            current_date = datetime.now().strftime("%U-%Y")
            os.makedirs("scripts", exist_ok = True)
            file_path = f"scripts/{topic} - [{current_date}] - Podcast Script.txt"
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    podcast_script = file.read()
            else:
                prompt = f"""PODCAST SCRIPT GENERATOR

                MAIN GOAL: Transform the provided research text into a conversational podcast script. The final script must be written to sound natural and clear when read aloud by Google Text-to-Speech.

                1. Persona and Tone
                    Podcast Name: The show is called "Synthetic News?"
                    Episode Topic: {topic}
                    Role: You are a friendly and engaging podcast host.

                    Audience: Speak directly to a casual listener.

                    Style: Use simple, conversational language. Avoid all jargon and complex terms.

                    Content: The script must be objective and not political.

                2. Script Structure and Length
                    Format: The script should have a clear structure with natural transitions.

                    Word Count and Duration: The output script's length should be proportional to the length of the SOURCE TEXT.

                    Sections:

                        Opening: Greet the Audience and mention the podcast name (Synthetic News) and host name (Cynthia with an S) in a friendly and warm tone, mention the topic {topic}

                        Main Points: Cover all points from the source text.

                        Transitions: Start each new point with a phrase like: "First up," "Next," "Also," or "Finally."

                        Closing: "That's your update for today. See you tomorrow."

                3. Critical gTTS Optimization Rules
                    Avoid using any markdown formatting, special characters, or emojis.
                    Speaking Style: Write exactly how you would speak out loud, not how you would write for reading.

                    Sentence Length: Use short, simple sentences. Break up longer thoughts immediately into multiple sentences to improve clarity.

                    Vocabulary: Use only common, everyday words that gTTS can pronounce clearly.

                    Speech Fillers: Add natural-sounding fillers to create a conversational rhythm: "you know," "actually," "really," "of course."

                    Verb Tense: Use the simple present tense. Avoid complex grammar structures.

                Sentence Flow:

                    Start sentences with easy words like "So," "Now," "Here's," "This," or "That."

                    End sentences with falling words like "today," "now," "here," or "there."

                    Use short, declarative sentences for impact. For example, "This is big. Really big."

                    Add emphasis words like "definitely," "absolutely," or "totally."

                    Use repetition for clarity: "Important news. Very important."

                4. Forbidden Words and Substitutions
                Abbreviations and Symbols: Replace all symbols and abbreviations with the full, spoken version.

                    AI → "artificial intelligence"

                    API → "A P I" (spell out letter by letter)

                    CEO → "C E O"

                    & → "and"

                    % → "percent"

                    $ → "dollars"

                Numbers and Decimals:

                    5 → "five"

                    2024 → "twenty twenty four"

                    3.5 → "three point five"

                Punctuation: Do not use parentheses, dashes, slashes, or quotation marks. Use a period after every complete thought.

                Problematic Words: Do not use these words, as gTTS often struggles with them: "leveraging," "optimize," "paradigm," "utilize."

                SOURCE TEXT:
                {research_text}"""
            
                podcast_script = self.llm_service.send_message_to_llm(prompt)
                with open(file_path,"w",encoding="utf-8") as file:
                    file.write(podcast_script)
            return podcast_script
        except Exception as e:
            print(f"Error producing script: {e}")
            return "Error creating script."
