class Graph:
    """
    used as a graph for the algorithm
    """
    def __init__(self, mat: list[list]):
        self.nodes = {-1: []}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if 0 < mat[i][j] < 1:
                    if self.nodes.keys().__contains__(i) is False:
                        self.nodes[i] = []
                    if self.nodes.keys().__contains__(j + len(mat)) is False:
                        self.nodes[j + len(mat)] = []
                    self.nodes[i].append(j + len(mat))
                    self.nodes[j + len(mat)].append(i)
        self.nodes.pop(-1)

    def getNeighbors(self, key: int):
        return self.nodes.get(key)


def hasCircle(mat: list[list]) -> bool:
    """
    >>> mat = [[1, 0.1, 0.07, 0],[0, 0.2, 0.93, 1]]
    >>> print(hasCircle(mat))
    i,j: 0,3 stack: [3] visited: {0}
    i,j: 0,4 stack: [3, 4] visited: {0}
    i,j: 0,0 stack: [3] visited: {0, 4}
    i,j: 0,1 stack: [3, 1] visited: {0, 4}
    True

    >>> mat = [[1, 1, 0.07, 0],[0, 0, 0.93, 1]]
    >>> print(hasCircle(mat))
    i,j: 0,4 stack: [4] visited: {0}
    i,j: 0,0 stack: [] visited: {0, 4}
    i,j: 0,1 stack: [1] visited: {0, 4}
    i,j: 0,4 stack: [] visited: {0, 1, 4}
    False

    based on DFS and helps with finding if divide has a circle in it
    aka more than n-1 connections

    """
    g: Graph = Graph(mat)
    all_visited = set()
    for i in range(len(mat)):
        # skip all of those who already visited
        if i not in all_visited:
            visited = set()
            stack = []
            visited = set()
            stack.append(i)
            while len(stack) > 0:
                node = stack.pop()
                visited.add(node)
                # go over all neighbors
                for j in g.getNeighbors(node):
                    # check that not checking origin node and that j isn't already visited
                    if j in stack:
                        return True
                    elif j not in visited:
                        stack.append(j)
                    print(f'i,j: {i},{j} stack: {stack} visited: {visited}')
            all_visited = all_visited.union(visited)

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()