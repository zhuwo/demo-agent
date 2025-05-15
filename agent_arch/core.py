from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from langchain_core.agents import AgentExecutor
import autogen

class DemoAgentCore:
    def __init__(self):
        self.documents = SimpleDirectoryReader('data').load_data()
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.engine = self.index.as_query_engine()
        
    def query(self, question: str) -> str:
        return self.engine.query(question)