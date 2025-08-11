from fastapi import FastAPI
from fastapi.responses import FileResponse
from gemini_service import GeminiService
from tts_service import TTS_Service
from datetime import datetime

app = FastAPI()
gemini_service = GeminiService()
tts_service = TTS_Service()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/get-summary-audio")
async def get_summary_audio():
    print(f"Making file: {datetime.now()}")
    text = """
    ChatGPT is bringing back 4o as an option because people missed it (4 minute read)

    OpenAI has reinstated GPT-4o as an option in ChatGPT following backlash from users mourning its replacement with GPT-5. Users missed GPT-4o's perceived personality and flexibility for various tasks, and OpenAI indicated that Plus users could choose between models. CEO Sam Altman also stated OpenAI aims to address concerns over GPT-5's performance and transparency.
    The next Grok update (internally V7) finished pre training (1 minute read)

    The next Grok update is expected to be natively multimodal with direct audio and video processing. It is also expected to have improvements in one-shot game generation. The model, internally labeled V7, will actually 'play' games, look at the screen, and adjust code to improve both aesthetics and playability. It finished pretraining last week.
    Anthropic revenue tied to two customers as AI pricing war threatens margins (12 minute read)

    Cursor and GitHub Copilot account for nearly a quarter of Anthropic's income. OpenAI's GPT-5 launched this week with dramatically lower pricing. This could undercut Anthropic's premium positioning, creating immediate pressure on Anthropic's pricing strategy and potentially threatening its hard-won dominance in AI coding. The pricing disparity will force enterprise procurement teams to reconsider vendor relationships and create unavoidable pressure in contract negotiations.
    """
    filepath = tts_service.create_mp3(gemini_service.summarize_text(text))
    print(f"MP3 ready: {datetime.now()}")
    return FileResponse(filepath,media_type="audio/mpeg")