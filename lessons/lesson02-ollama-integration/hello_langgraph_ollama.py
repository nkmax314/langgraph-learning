from typing import TypedDict

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph


# Define state
class State(TypedDict):
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
        [HumanMessage(content=state.get("question", "Why is the sky blue?"))]
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
result = graph.invoke({"question": "Explain LangGraph in simple terms."})


print("\nQuestion:")
print(result["question"])

print("\nAnswer:")
print(result["answer"])
