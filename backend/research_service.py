from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
from datetime import datetime
from abc import ABC, abstractmethod

class TaskProvider(ABC):
    @abstractmethod
    def task(self):
        pass

class ResearchService(TaskProvider):
    def __init__(self):
        print("Initializing Reaserch Agent...")

        load_dotenv()
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            print("Error: GEMINI_API_KEY not found in .env")
            exit()
        # Set up LLM and Tools
        try:

            self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=gemini_api_key, temperature = 0)
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            exit()
        # Set up tools
        self.search_tool = TavilySearchResults()
        self.tools = [self.search_tool]

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI news researcher specializing in BREAKING and RECENT news. 
            
            CRITICAL INSTRUCTIONS:
            - Only search for news from the last week.
            - Use search terms like "today", "yesterday", "breaking news", "latest"
            - Prioritize news from the current date: {current_date}
            - If you find older news, explicitly search again with more recent terms
            - Always mention the publication date of articles
            - Focus on live, developing stories and fresh updates"""),
            ("placeholder", "{chat_history}"),
            ("human", "Find the most recent news (last week) about: {input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])
        
        self.agent = create_tool_calling_agent(self.llm,self.tools,self.prompt)

        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.tools, verbose=True)

    def run_research(self,topic):

        print(f"\n{datetime.now()}: Starting research on: '{topic}'...")
        try:
            current_date = datetime.now().strftime("%d-%m-%Y")
            os.makedirs('summaries',exist_ok=True)
            summary_file_path = f'summaries/{topic} - [{current_date}] - Research Text.txt'
            if os.path.exists(summary_file_path):
                # read and return
                with open(summary_file_path,'r', encoding="utf-8") as file:
                    final_summary = file.read()
            else:
                response = self.agent_executor.invoke({"input": topic, "current_date":current_date})
                final_summary = response['output']
                with open(summary_file_path,'w', encoding="utf-8") as file:
                    file.write(final_summary)
            
            return final_summary
        except Exception as e:
            print(f"Error running research: {e}")
            return "Failed to complete research"
    
    def task(self):
        return self.run_research("AI")
