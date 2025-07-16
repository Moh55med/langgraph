from langgraph.graph import StateGraph, END
from agents import agent_total_tourists, agent_divide_tourists, agent_nation_chart, agent_month_chart

def main():
    graph = StateGraph()
    graph.add_node("total_tourists", agent_total_tourists)
    graph.add_node("divide_tourists", agent_divide_tourists)
    graph.add_node("nation_chart", agent_nation_chart)
    graph.add_node("month_chart", agent_month_chart)

    graph.add_edge("total_tourists", "divide_tourists")
    graph.add_edge("divide_tourists", "nation_chart")
    graph.add_edge("nation_chart", "month_chart")
    graph.add_edge("month_chart", END)

    workflow = graph.compile()
    result = workflow.invoke({})
    print("Workflow complete. Results:")
    print(result)

if __name__ == "__main__":
    main() 