from typing import TypedDict

from langgraph.graph import END, START, StateGraph


# 1 Define the state
class State(TypedDict):
    message: str


# Define a node


def hello_world(state: State):
    print("Executing Hello World Node...")

    return {"message": "Hello World from LangGraph!"}


# 3. Create the graph
graph_builder = StateGraph(State)


# 4. Add the node
graph_builder.add_node("hello_world", hello_world)


# 5. Connect the nodes
graph_builder.add_edge(START, "hello_world")
graph_builder.add_edge("hello_world", END)


# 6. Compile the graph
graph = graph_builder.compile()


# 7. Execute the graph
result = graph.invoke({"message": "Starting LangGraph"})


print("\nFinal Result:")
print(result)
