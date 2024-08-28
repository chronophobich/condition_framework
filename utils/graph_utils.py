import networkx as nx

from core.parser import parse_variables


# Function to build the dependency graph sub_condition
def build_dependency_graph(sub_conditions, default_values):
    graph = nx.DiGraph()
    for sub_condition in sub_conditions:
        lhs, rhs = parse_variables(sub_condition)

        if "=" in sub_condition and "==" not in sub_condition:
            graph.add_edge(rhs, lhs)
        elif rhs in default_values:
            graph.add_edge(rhs, lhs)
        else:
            graph.add_node(lhs)

    return graph
