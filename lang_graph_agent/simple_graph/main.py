from typing import TypedDict, Literal
import random
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    graph_state: str


def node_1(state):
    print("Node 1 is being executed.")
    return {"graph_state": state["graph_state"] + "I am "}


def node_2(state):
    print("Node 2 is being executed.")
    return {"graph_state": state["graph_state"] + "a simple graph."}


def node_3(state):
    print("Node 3 is being executed.")
    return {"graph_state": state["graph_state"] + "This is the end."}


def decide_mood(state) -> Literal["node_2", "node_3"]:
    user_input = state["graph_state"]

    if random.random() < 0.5:
        return "node_2"

    return "node_3"


builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)


graph = builder.compile()


def main():
    print(graph.invoke({"graph_state": "Mitesh - "}))
    # Show the graph visually if possible
    # try:
    #     img = graph.get_graph().to_image()
    #     display(img)
    # except Exception as e:
    #     print("Could not display image. Showing text representation instead.")
    #     print(graph.get_graph())


if __name__ == "__main__":
    main()
