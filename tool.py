from langchain_community.tools import tool
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
from rich import print
# Load environment variables (.env file)
# Mistral API key is stored here

load_dotenv()
# ==================================================
# Tool 1: Count the length of a given text

@tool
def len_of_text(text : str) -> int:
    """The tool is used to count the lenth of the charcter in the given text"""
    return len(text)

# ==================================================
# Tool 2: Multiply two numbers
@tool
def multiply(a : int, b : int)-> int:
    """This tool is used to multiply any two numbers """
    return a * b 
# ==================================================
# Store all tools in a dictionary
# This helps us execute tools dynamically
# based on the tool name returned by the LLM
tools = {
    "len_of_text" : len_of_text,
    "multiply"    : multiply
}

# ==================================================
# Initialize Mistral LLM
llm = ChatMistralAI(model="mistral-small")
# ==================================================
# Bind all the tools with the LLM
# Now the model can decide when to use a tool
llm_with_tool = llm.bind_tools([len_of_text,multiply])
#========================================================
# create a message history
message = []
prompt = input("you : ")
# Convert user input into a HumanMessage
query  = HumanMessage(prompt)

message.append(query)
# First LLM Call
# The model decides whether it needs a tool
result = llm_with_tool.invoke(message)

message.append(result)
# Check if the model requested a tool
if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)
    # now llm take all the message(Humanmessage,AImessage,Toolmessage) and give the final result
    responce  = llm_with_tool.invoke(message)
    print(responce.content)









