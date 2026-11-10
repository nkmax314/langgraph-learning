from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph


# Define state
class State(TypedDict):
    topic: str
    question: str
    answer: str


# initialize llm
llm = ChatOllama(
    model="llama3.2",
    temperature=0.7,
)


# Define LLM node
def llm_node(state: State):
    print("Executing LLM node...")

    response = llm.invoke(
        [
            SystemMessage(content="You are a Python programming language tutor."),
            HumanMessage(content=state["question"]),
        ],
    )

    return {"answer": response.content}


# Create graph
# 4. Create graph
graph_builder = StateGraph(State)


# 5. Add node

graph_builder.add_node("llm_node", llm_node)


# 6. Define edges
graph_builder.add_edge(START, "llm_node")
graph_builder.add_edge("llm_node", END)


# 7. Compile graph
graph = graph_builder.compile()


# 8. Execute graph
topic = "Decorators"
question = input(" Enter your question\n")
result = graph.invoke({"topic": "topic", "question": question})


print("\nQuestion:")
print(result["question"])

print("\nAnswer:")
print(result["answer"])
