import os
from abc import ABC, abstractmethod
from datetime import datetime
from gtts import gTTS

class TTS_Service(ABC):
    @abstractmethod
    def convert_text_to_speech(self,text):
        pass
"""
    This class's main purpose is to convert text to speech.
"""
class gTTS_Service(TTS_Service):
    DEFAULT_OUTPUT_DIR = "generated_audio"
    def __init__(self):
        self.output_dir = self.DEFAULT_OUTPUT_DIR
        os.makedirs(self.output_dir, exist_ok=True)

    """
        Receives a text input, creates an mp3 speech file and returns
        the path to that file.
    """
    def convert_text_to_speech(self,text):
        tts = gTTS(text=text, lang="en", slow=False)
        return tts

    def create_mp3(self, topic, text):
        os.makedirs(self.output_dir, exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%U-%Y")
        filename = f"{topic} - [{timestamp}] - Audio.mp3"
        filepath = os.path.join(self.output_dir, filename)
        if (not os.path.exists(filepath)):
            tts = self.convert_text_to_speech(text)
            tts.save(filepath)

        return filepath

class GoogleLM_TTS_Service(TTS_Service):
    def convert_text_to_speech(self, text):
        return super().convert_text_to_speech(text)