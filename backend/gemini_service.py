import os
from datetime import datetime
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

    def generate_podcast_script(self, topic, research_text):
        try:
            current_date = datetime.now().strftime("%d-%m-%Y")
            os.makedirs("scripts", exist_ok = True)
            file_path = f"scripts/{topic} - [{current_date}] - Podcast Script.txt"
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    podcast_script = file.read()
            else:
                prompt = f"""Transform this research text into an engaging podcast script for text-to-speech conversion.

                REQUIREMENTS:
                - Write as a friendly podcast host speaking directly to listeners
                - Use simple, conversational language - avoid jargon or complex terms
                - Structure with clear sections and natural transitions
                - Keep total length of 5 minutes when spoken (roughly 625-750 words)
                - Be Objective and not political

                TTS OPTIMIZATION:
                - Avoid using any markdown formatting, special characters, or emojis. 
                - Use periods for natural pauses, not commas in long sentences
                - Spell out numbers and abbreviations (AI becomes "artificial intelligence")
                - Add transition phrases like "Now," "Here's what's interesting," "Moving on"
                - Break up long sentences into shorter ones for better flow


                STRUCTURE:
                1. Brief engaging opening (15-20 words)
                2. 3-4 main points with smooth transitions between them
                3. Conclude with key takeaway or forward-looking statement

                TONE: Enthusiastic but informative, like explaining exciting news to a friend

                SOURCE TEXT:
                {research_text}

                Create the podcast script now:"""
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
            
                response = self.model.generate_content(prompt)
                podcast_script = response.text
                with open(file_path,"w",encoding="utf-8") as file:
                    file.write(podcast_script)
            return podcast_script
        except Exception as e:
            print(f"Error producing script: {e}")
            return "Error creating script."