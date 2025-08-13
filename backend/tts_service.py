import os
from gtts import gTTS
from datetime import datetime
from abc import ABC, abstractmethod

class TTS_Service(ABC):
    @abstractmethod
    def text_to_speech(self,text):
        pass

class gTTS_Service(TTS_Service):
    def __init__(self, output_dir="generated_audio"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def text_to_speech(self,text):
        tts = gTTS(text=text, lang="en", slow=False)
        return tts

    def create_mp3(self, topic, text):
        os.makedirs(self.output_dir, exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%U-%Y")
        filename = f"{topic} - [{timestamp}] - Audio.mp3"
        filepath = os.path.join(self.output_dir, filename)
        if (not os.path.exists(filepath)):
            tts = self.text_to_speech(text)
            tts.save(filepath)

        return filepath

class GoogleLM_TTS_Service(TTS_Service):
    def text_to_speech(self, text):
        return super().text_to_speech(text)