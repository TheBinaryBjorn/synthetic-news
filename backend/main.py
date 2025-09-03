"""
This module provides a FastAPI application to serve podcast summaries.
It handles requests to generate and retrieve audio files based on a given topic.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse

from .services.exceptions import (ResearchException, ScriptWriterException,
                                 TopicException, TtsException)
from .services.service_manager import ServiceManager

app = FastAPI()
service_manager = ServiceManager()


@app.get("/")
def read_root():
    """
    Handles the root endpoint to confirm the API is running.
    """
    return {"Hello": "World"}


@app.get("/get-summary-audio")
async def get_summary_audio(topic: str):
    """
    Generates an audio file of a podcast summary for a given topic.

    Args:
        topic (str): The topic for the podcast summary.
                     Underscores are replaced with spaces.

    Returns:
        FileResponse: An audio file of the podcast summary.
        dict: An error message if the operation fails.
    """
    topic = topic.replace("_", " ")
    try:
        audio_file_path = service_manager.produce_podcast(topic)
        return FileResponse(audio_file_path, media_type="audio/mpeg")
    except (
        ResearchException,
        ScriptWriterException,
        TtsException,
        TopicException,
    ) as e:
        return {"error": f"{e}"}
