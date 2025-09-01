"""
This Module provides a management service to all services used in
the program.
It handles the production of the podcast episode by utilizing
all the services made.
"""

from datetime import datetime

from .exceptions import (ResearchException, ScriptWriterException,
                         TopicException, TtsException)
from .llm_service import GeminiService
from .research_service import TavilyResearchService
from .script_writer_service import GeminiWriterService
from .tts_service import GoogleTtsService


class ServiceManager:
    """
    Manages all services to produce a podcast episode from a given topic.
    """

    def __init__(self):
        self.research_service = TavilyResearchService()
        self.script_writer_service = GeminiWriterService(GeminiService())
        self.tts_service = GoogleTtsService()
        self.allowed_topics = [
            "AI",
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
            "Databases",
        ]

    def produce_podcast(self, topic):
        """
        Produces and mp3 file based on the given topic by utilizing all services.
        """
        if topic in self.allowed_topics:
            print(f"Making file: {datetime.now()}")
            try:
                research_text = self.research_service.run_research(topic)
            except Exception as e:
                raise ResearchException(e) from e
            try:
                podcast_script = self.script_writer_service.generate_podcast_script(
                    topic, research_text
                )
            except Exception as e:
                raise ScriptWriterException(e) from e
            try:
                filepath = self.tts_service.create_mp3(topic, podcast_script)
            except Exception as e:
                raise TtsException(e) from e
            print(f"MP3 ready: {datetime.now()}")
            return filepath
        raise TopicException("Topic not allowed.")
