from fastapi import FastAPI
from fastapi.responses import FileResponse
from services.service_manager import ServiceManager

app = FastAPI()
service_manager = ServiceManager()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/get-summary-audio")
async def get_summary_audio(topic: str):
    # Replace all occourances of '_' with ' '
    topic = topic.replace("_"," ")
    try:
        audio_file_path = service_manager.produce_podcast(topic)
        return FileResponse(audio_file_path,media_type="audio/mpeg")
    except Exception as e:
        return {"error":f"{e}"}
    