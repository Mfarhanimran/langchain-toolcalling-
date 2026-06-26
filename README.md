# LangChain Tool Calling with Mistral AI

A beginner-friendly project demonstrating **Tool Calling** using **LangChain** and **Mistral AI**.

The Large Language Model (LLM) can decide when to call external tools, execute them, and use their outputs to generate a final response.



## Features

* Count the length of any text
* Multiply two numbers
* Dynamic tool selection
* Tool execution loop
* Message history management
* Mistral AI integration
* LangChain Tool Binding



## Technologies Used

* Python
* LangChain
* Mistral AI
* dotenv
* Rich



## Project Structure


project/
│
├── main.py
├── .env
├── requirements.txt
└── README.md




## How It Works

1. User enters a prompt.
2. The prompt is converted into a `HumanMessage`.
3. The LLM analyzes the request.
4. If a tool is needed, it returns a `tool_call`.
5. The corresponding Python function is executed.
6. A `ToolMessage` is added to the conversation.
7. The LLM receives the tool output and generates the final response.

Workflow:


HumanMessage
      │
      ▼
 Mistral AI
      │
      ▼
Tool Call
      │
      ▼
Python Tool
      │
      ▼
ToolMessage
      │
      ▼
 Final AI Response


## Available Tools

### 1. Text Length Tool

Counts the number of characters in a string.

len_of_text(text)

Example:

Input:
Hello World

Output:
11

---

### 2. Multiply Tool

Multiplies two integers.

multiply(a, b)

Example:

Input:
12 × 8

Output:
96

## Installation

Clone the repository

bash
git clone https://github.com/yourusername/repository-name.git

Install dependencies

bash
pip install -r requirements.txt


Create a `.env` file

text
MISTRAL_API_KEY=your_api_key


Run the project

bash
python main.py




## Learning Outcomes

This project helped me understand:

* LangChain Tools
* Tool Binding
* AIMessage
* HumanMessage
* ToolMessage
* Tool Calling
* Agent Workflow
* Message History
* LLM Decision Making



## Future Improvements

* Add more tools
* Weather API Tool
* Calculator Tool
* Search Tool
* File Reader Tool
* Multi-tool support
* Memory
* AI Agent



## Author

Farhan Imran

Currently learning AI Engineering by building real-world projects with Python, LangChain, LLMs, RAG, and AI Agents.

⭐ If you found this project useful, consider giving it a star!
