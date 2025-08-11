import os
from gtts import gTTS
from datetime import datetime

class TTS_Service:
    def __init__(self, output_dir="generated_audio"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create_mp3(self, text):
        tts = gTTS(text=text, lang="en", slow=False)
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"tldr_summary_{timestamp}.mp3"
        filepath = os.path.join(self.output_dir, filename)
        tts.save(filepath)
        return filepath