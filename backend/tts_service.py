import os
from gtts import gTTS
from datetime import datetime

class TTS_Service:
    def __init__(self, output_dir="generated_audio"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create_mp3(self, topic, text):
        os.makedirs(self.output_dir, exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y")
        filename = f"{topic} - [{timestamp}] - Audio.mp3"
        filepath = os.path.join(self.output_dir, filename)
        if (not os.path.exists(filepath)):
            tts = gTTS(text=text, lang="en", slow=False)
            tts.save(filepath)

        return filepath