"""
This Module is in charge of all Text to Speech classes and
methods.
"""

import os
from abc import ABC, abstractmethod
from datetime import datetime

from gtts import gTTS


class TtsService(ABC):
    """
    Abstract base class for all Text-to-Speech services.
    """

    @abstractmethod
    def convert_text_to_speech(self, text):
        pass


class GoogleTtsService(TtsService):
    """
    A concrete implementation of TtsService that uses the gTTS library.
    """

    DEFAULT_OUTPUT_DIR = "generated_audio"

    def __init__(self):
        """
        Initializes the service and creates the output directory if it doesn't exist.
        """
        self.output_dir = self.DEFAULT_OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_text_to_speech(self, text: str) -> gTTS:
        """
        Receives a text input and creates an mp3 speech file.

        Args:
            text (str): The text to convert to speech.

        Returns:
            gTTS Object.
        """
        if not isinstance(text, str):
            raise TypeError
        tts = gTTS(text=text, lang="en", slow=False)
        return tts

    def create_mp3(self, topic: str, text: str):
        """
        Generates and saves an MP3 file from text.

        Args:
            topic (str): The topic used for the filename.
            text (str): The text to be converted to speech.

        Returns:
            str: The file path of the saved MP3 file.
        """
        os.makedirs(self.output_dir, exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%U-%Y")
        filename = f"{topic} - [{timestamp}] - Audio.mp3"
        filepath = os.path.join(self.output_dir, filename)
        if not os.path.exists(filepath):
            tts = self.convert_text_to_speech(text)
            tts.save(filepath)

        return filepath
