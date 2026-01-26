import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch(api_key=TAVILY_API_KEY)]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Welcome to the Search Agent!")
    prompt = "search for 3 job postings for an ai engineer using langchain in the Vietnam area on linkedin and list their details?"
    result = agent.invoke(input={"messages": [HumanMessage(content=prompt)] })
    print(result)
    pass

if __name__ == "__main__":
    main()