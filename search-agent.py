import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


llm = ChatOpenAI(model="gpt-4o")
tools = [TavilySearch(api_key=TAVILY_API_KEY)]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Welcome to the Search Agent!")
    prompt = "HoangSa and TruongSa are located in which country? and I want you to respond in Vietnamese."
    result = agent.invoke(input={"messages": [HumanMessage(content=prompt)] })
    print(result["messages"][len(result["messages"]) - 1].content)
    pass

if __name__ == "__main__":
    main()