from typing import List

import matplotlib.pyplot
import networkx as nx


def build_graph(valuations: List[List[int]]) -> nx.DiGraph:
    range_j = len(valuations[0])
    range_i = len(valuations)
    g = nx.DiGraph()
    for i in range(range_i):
        g.add_edges_from([(i, f'{i}'), (f'{i}', i)])
        for j in range(range_j):
            if valuations[i][j] > 0:
                g.add_edge(i, f'{j}')
    return g


def final_strongly_connected_componenets(g: nx.DiGraph):
    """
    >>> valuations = [[1, 0, 7, 0, 0, 0], [7, 7, 0, 7, 0, 0], [0, 0, 7, 0, 7, 0],[0, 0, 7, 0, 0, 0], [7, 0, 0, 0, 0, 7],[0, 7, 0, 0, 0, 0]]
    >>> D = build_graph(valuations)
    >>> print(final_strongly_connected_componenets(D))
    True



    >>> valuations1 = [[1, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0], [0, 0, 7, 0, 0, 0],[0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 7, 0],[0, 0, 0, 0, 0, 7]]
    >>> D2 = build_graph(valuations1)
    >>> print(final_strongly_connected_componenets(D2))
    False
    """
    strongly_connected_componenets = nx.strongly_connected_components(g)
    components_are_final: List[bool] = []
    # component_final = None
    flag = True
    # check each component
    for component in strongly_connected_componenets:
        # check for each component for each node
        # no edges from Component to other components
        # edge from player to his house
        if component.__len__() == 2:
            comp = [x for x in component]
            if type(comp[0]) == int and type(comp[1]) == str:
                if f'{comp[0]}' == comp[1]:
                    flag = False
            elif type(comp[0]) == str and type(comp[1]) == int:
                if f'{comp[1]}' == comp[0]:
                    flag = False
        else:
            for node in component:
                edges_id = [y for x, y in g.edges(node)]
                # check edge out of the component
                for i in edges_id:
                    if i not in component:
                        flag = False
                        break
                if type(node) == int:
                    if edges_id.__contains__(f'{node}') is False:
                        flag = False
                        break
        components_are_final.append(flag)
        # if flag:
        #     component_final = component
        flag = True
    return components_are_final.__contains__(True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
