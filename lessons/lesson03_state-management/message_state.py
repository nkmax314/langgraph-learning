from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, MessagesState, StateGraph

# initialize LLM
llm = ChatOllama(model="llama3.2", temperature=0.7)


# Define llm node
def tutor_node(state: MessagesState):
    print("Executing Tutor Node...")
    system_message = SystemMessage(
        content="You are an experienced Python programming tutor."
    )
    # Combine system instructions with conversation history
    messages = [system_message, *state["messages"]]

    response = llm.invoke(messages)

    # return the new AI message
    return {"messages": [response]}


# 3. Create graph
graph_builder = StateGraph(MessagesState)


# 4. Add node
graph_builder.add_node("tutor_node", tutor_node)


# 5. Define edges
graph_builder.add_edge(START, "tutor_node")
graph_builder.add_edge("tutor_node", END)


# 6. Compile graph
graph = graph_builder.compile()


# 7. Execute graph
question = input("\nAsk your Python tutor: ")

result = graph.invoke({"messages": [HumanMessage(content=question)]})


# 8. Display conversation
print("\nConversation:")

for message in result["messages"]:
    print(f"\n{message.type}: {message.content}")
