import random


def DFS(value_matrix: list[list]) -> list:
    """
    run until until get to leaf
    if leaf is optimal then stop run and return the path of dividing the items
    not optimal then:
        if  last leaf in group go one group up and try the others
        not last leaf in group then try next leaf
    :param value_matrix: the value matrix for value a player gave to each item
    :return: optimal divide
    """
    option_set = set()
    tree_stack = [[
        0,  # items divided
        0,  # value for player 1
        0,  # value for player 2
        0,  # num of visits
        0,  # gave to which player
    ]]
    while len(tree_stack) != 0:
        v = tree_stack.pop()
        # 1) check if number item in v is equal to number of items
        # 1.1) not equal then -> create all children of current v and push them into stack and repeat
        # 1.2) equal then check if optimal
        # 1.2.1) optimal return path
        # 1.2.2) not optimal continue running
        if v[0] == len(value_matrix[0]):
            print("optimal check")
            optimal_divide, is_optimal = check_optimal(value_matrix, tree_stack, v)
            if is_optimal:
                return optimal_divide
        if v[3] != len(value_matrix):
            tree_stack.append([v[0], v[1], v[2], v[3] + 1, v[4]])
            # index of item to divide
            item_index = v.__getitem__(0) + 1
            # first child
            tree_stack.append([item_index, v[] + value_matrix[v[3]], [item_index - 1], 0, v[3]])


def check_optimal(value_matrix, tree_stack, v) -> (list, bool):
    for i in range(len(value_matrix)):
        # 1/n <= value for player
        if 1/sum(value_matrix[i]) > v[i+1]/sum(value_matrix[i]):
            return [], False
    path = [v[]]
    while len(tree_stack) > 0:

    return path.reverse(), True


a = random.Random().random().__round__(4)
number_of_items = 10
value = 1
root = (
    0,  # player 1 value
    0,  # player 2 value
    0)  #
if __name__ == '__main__':
    print("")
