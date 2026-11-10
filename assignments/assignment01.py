from typing import TypedDict

from langgraph.graph import END, START, StateGraph


# 1 Define the state
class State(TypedDict):
    name: str
    message: str


# Define node 1


def node1(state: State):
    print("Executing First Node...")
    name = input("\n Enter the user's name: \n")
    return {"name": name, "message": f"Hello {name}!"}


# Define node 1


def node2(state: State):
    print("Executing Second Node...")

    return {
        "name": state.get("name"),
        "message": state.get("message") + " Welcome to LangGraph!",
    }


# 3. Create the graph
graph_builder = StateGraph(State)


# 4. Add the node
graph_builder.add_node("node1", node1)
graph_builder.add_node("node2", node2)


# 5. Connect the nodes
graph_builder.add_edge(START, "node1")
graph_builder.add_edge("node1", "node2")
graph_builder.add_edge("node2", END)


# 6. Compile the graph
graph = graph_builder.compile()


# 7. Execute the graph
result = graph.invoke({"message": "Starting LangGraph"})


print("\nFinal Result:")
print(result)
