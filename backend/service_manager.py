from research_service import TavilyResearchService
from script_writer_service import GeminiWriterService
from tts_service import gTTS_Service
from datetime import datetime

class ServiceManager():
    def __init__(self):
        self.research_service = TavilyResearchService()
        self.script_writer_service = GeminiWriterService()
        self.tts_service = gTTS_Service()
        self.allowed_topics = ["AI", 
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
    
    def produce_podcast(self,topic):
        if(topic in self.allowed_topics):
            try:
                print(f"Making file: {datetime.now()}")
                research_text = self.research_service.run_research(topic)
                podcast_script = self.script_writer_service.generate_podcast_script(topic, research_text)
                filepath = self.tts_service.create_mp3(topic, podcast_script)
                print(f"MP3 ready: {datetime.now()}")
                return filepath
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception("Topic not allowed.")
