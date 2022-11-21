import random


def is_optimal(v, value_m) -> bool:
    """
    checks if current state is a proportional divide of values
    :param v: current state
    :param value_m: value matrix
    :return:
    """
    div = 1 / len(value_m)
    for i in range(len(value_m)):
        player_value_sum = sum(value_m[i])
        if div > v[i + 1] / player_value_sum:
            return False
    return True


def check_change(curr, prev):
    """
    checks which player value changed and return the index
    :param curr:
    :param prev:
    :return:
    """
    for i in range(1, len(prev) - 1):
        if curr[i] > prev[i]:
            return i


def get_path(tree_stack, curr):
    """
    traverses stack to build divide path of items to players
    :param tree_stack:
    :param curr: current leaf
    :return:
    """
    path = []
    prev = tree_stack.pop()
    while len(tree_stack) > 0 and curr[0] != 0:
        path.append(check_change(curr, prev))
        curr = prev
        prev = tree_stack.pop()
    return path


def dfs_optimal_search(value_m: list[list]) -> list:
    v = [0, 0, 0, 0]
    tree_stack = [v]
    while len(tree_stack) > 0:
        v = tree_stack.pop()
        # check if node is a leaf and if a leaf then check for optimal solution
        if v[0] == len(value_m[0]):
            if is_optimal(v, value_m):
                path = get_path(tree_stack, v)
                path.append(v[len(v) - 1] + 1)
                path.reverse()
                return path
        elif v[3] < len(value_m) and v[0] < len(value_m[0]):
            new_v = [v[0], v[1], v[2], 0]
            # player index to increase the item value of
            index = v[3]
            # increase visit count and push parent node back into stack
            v[3] = v[3] + 1
            tree_stack.append(v)
            # handle the new node to use
            # increase value of player
            new_v[index + 1] = new_v[index + 1] + value_m[index][new_v[0]]
            # increase item count
            new_v[0] = new_v[0] + 1
            # reset visit count
            new_v[3] = 0
            # add new node to tree stack
            tree_stack.append(new_v)
        return []


if __name__ == '__main__':
    value_matrix = [
        [11, 22, 33],
        [11, 22, 33]
    ]
    print(dfs_optimal_search(value_matrix))

    print("")
