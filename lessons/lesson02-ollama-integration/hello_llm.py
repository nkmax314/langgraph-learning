from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

# initialize ollama
llm = ChatOllama(model="llama3.2", temperature=0.7)

# create a message
messages = [HumanMessage(content="Explain what an AI agent is, in simple terms.")]

# Invoke LLM
response = llm.invoke(messages)

print("LLM Response")
print(response.content)
