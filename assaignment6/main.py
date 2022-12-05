from typing import List

import networkx as nx
from networkx import NetworkXNoCycle


def find_cycle_in_consumption_graph(allocation: List[List[float]]) -> List[int]:
    """
    >>> mat = [[1, 0.1, 0.07, 0],[0, 0.2, 0.93, 1]]
    >>> print(find_cycle_in_consumption_graph(mat))
        [(1, 4), (4, 2), (2, 5), (5, 1)]


    >>> mat = [[1, 1, 0.07, 0],[0, 0, 0.93, 1]]
    >>> print(find_cycle_in_consumption_graph(mat))
    []

    uses networkx built-in support to find cycles in the graph
    if a cycle exit in the graph return the cycle
    if there is no cycle in the graph return empty list
    """
    g = nx.Graph()
    for i in range(len(allocation)):  # row
        for j in range(len(allocation[0])):  # column
            if 1 > allocation[i][j] > 0:
                g.add_edge(u_of_edge=j, v_of_edge=i + len(allocation[0]))

    try:
        return nx.find_cycle(g)
    except NetworkXNoCycle:
        return []


if __name__ == "__main__":
    import doctest
    doctest.testmod()

