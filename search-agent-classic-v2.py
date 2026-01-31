from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_STRUCTURED_TOOL_CALLS
from schemas import AgentResponse

load_dotenv()

tavily_search = TavilySearch()
llm = ChatOpenAI(model="gpt-4")
structure_llm = llm.with_structured_output(AgentResponse)
# output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instruction = PromptTemplate(
    template=REACT_PROMPT_WITH_STRUCTURED_TOOL_CALLS,
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
).partial(format_instructions="")

# react_prompt_with_format_instruction = PromptTemplate(
#     template=REACT_PROMPT_WITH_STRUCTURED_TOOL_CALLS,
#     input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
# ).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(
    llm=llm,
    tools=[tavily_search],
    prompt=react_prompt_with_format_instruction,
)

agent_executor = AgentExecutor(agent=agent, tools=[tavily_search], verbose=True)
extract_output = RunnableLambda(lambda x: x["output"])
# parse_output = RunnableLambda(lambda x: output_parser.parse(x))  # type: ignore

chain = agent_executor | extract_output | structure_llm


def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )
    assert isinstance(result, AgentResponse)
    if result:
        print(result.answer)
        print(result.sources)


if __name__ == "__main__":
    main()
