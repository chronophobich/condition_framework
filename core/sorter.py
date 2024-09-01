import networkx as nx

from core.parser import parse_variables
from utils.graph_utils import build_dependency_graph


# Function to topologically sort each condition
def sort_sub_conditions(condition, default_values):
    condition = condition.replace(" AND ", " and ")
    sub_conditions = condition.split(" and ")
    graph = build_dependency_graph(sub_conditions, default_values)
    try:
        ordered_sub_conditions = list(nx.topological_sort(graph))
        ordered_condition = " and ".join([sub_condition for sub_condition in sub_conditions if
                                          parse_variables(sub_condition)[0] in ordered_sub_conditions])
        
        return ordered_condition
    except nx.NetworkXUnfeasible:
        print("Cycles was detected in the sub_conditions. Solution Might not exist")
        return condition
