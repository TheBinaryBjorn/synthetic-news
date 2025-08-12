from fastapi import FastAPI
from fastapi.responses import FileResponse
from gemini_service import GeminiService
from tts_service import TTS_Service
from datetime import datetime
from research_service import ResearchService

app = FastAPI()
gemini_service = GeminiService()
tts_service = TTS_Service()
research_service = ResearchService()
allowed_topics = ["AI", 
                  "Artificial Intelligence", 
                  "Low Level Programming", 
                  "Frontend Development", 
                  "Backend Development", 
                  "Fullstack Development", 
                  "Machine Learning", 
                  "Data Science", 
                  "Cloud Computing", 
                  "DevOps", 
                  "Cybersecurity", 
                  "Mobile Development", 
                  "Game Development", 
                  "Web Development", 
                  "Blockchain", 
                  "Data Engineering", 
                  "Databases"
                  ]

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/get-summary-audio")
async def get_summary_audio(topic: str):
    # Replace all occourances of '_' with ' '
    topic = topic.replace("_"," ")
    if(topic in allowed_topics):
        print(f"Making file: {datetime.now()}")
        research_text = research_service.run_research(topic)
        podcast_script = gemini_service.generate_podcast_script(topic, research_text)
        filepath = tts_service.create_mp3(topic, podcast_script)
        print(f"MP3 ready: {datetime.now()}")
        return FileResponse(filepath,media_type="audio/mpeg")
    else:
        return {"error":"Topic not in allowed list."}