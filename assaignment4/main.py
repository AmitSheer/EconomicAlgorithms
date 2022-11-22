

def is_optimal(v, value_m) -> bool:
    """
    checks if current state is a proportional divide of values

    >>> v = [3, 11, 11]
    >>> value_m = [[11,11],[11,11]]
    >>> is_optimal(v,  value_m)
    True

    >>> v = [3, 14, 11]
    >>> value_m = [[11,11],[11,14]]
    >>> is_optimal(v,  value_m)
    False

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
    >>> curr = [2,1,3,3]
    >>> prev = [2,1,2,3]
    >>> check_change(curr, prev)
    2

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

    >>> tree_stack = []
    >>> tree_stack.append([0,0,0,0])
    >>> tree_stack.append([1,11,0,0])
    >>> curr = [2,11,11,0]
    >>> get_path(tree_stack, curr)
    [2]

    returned the path from current to the top without current

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


# ------------------------ Q1 ------------------------------
def dfs_optimal_search(value_m: list[list], pruning: bool = False) -> list:
    """
    lets use a simple matrix for this solution
    this will give us the best way to divide the items
    >>> dfs_optimal_search([[11, 11, 11, 11, 11, 11, 11, 11],[11, 11, 11, 11, 11, 11, 11, 11]])
    number of states calculated when pruning was: False, num of states: 35
    [1, 1, 1, 1, 2, 2, 2, 2]


    this will give us best way to divide items with the number of states it calculated we can see that the number
    is indeed different by almost 10 to the first search without the pruning
    >>> dfs_optimal_search([[11, 11, 11, 11, 11, 11, 11, 11],[11, 11, 11, 11, 11, 11, 11, 11]], True)
    number of states calculated when pruning was: True, num of states: 25
    [1, 1, 1, 1, 2, 2, 2, 2]

    more examples:
    >>> dfs_optimal_search([[11, 22, 33, 44, 55, 66, 77, 88], [11, 22, 33, 44, 55, 66, 77, 88]])
    number of states calculated when pruning was: False, num of states: 34
    [1, 1, 1, 1, 2, 2, 2, 1]


    >>> dfs_optimal_search([[11, 22, 33, 44, 55, 66, 77, 88], [11, 22, 33, 44, 55, 66, 77, 88]], True)
    number of states calculated when pruning was: True, num of states: 34
    [1, 1, 1, 1, 2, 2, 2, 1]
    """
    v = [0, 0, 0, 0]
    tree_stack = [v]
    number_of_states = 1
    all_states = dict()
    while len(tree_stack) > 0:
        v = tree_stack.pop()
        # check if node is a leaf and if a leaf then check for optimal solution
        if v[0] == len(value_m[0]):
            if is_optimal(v, value_m):
                path = get_path(tree_stack, v)
                path.append(v[len(v) - 1] + 1)
                path.reverse()
                # print(all_states)
                print(f'number of states calculated when pruning was: {pruning}, num of states: {number_of_states}')
                return path
        elif v[3] < len(value_m) and v[0] < len(value_m[0]):
            new_v = [v[0], v[1], v[2], 0]
            # player index to increase the item value of
            index = v[len(v) - 1]
            # increase visit count and push parent node back into stack
            v[len(v) - 1] = v[len(v) - 1] + 1
            tree_stack.append(v)
            # handle the new node to use
            # increase value of player
            new_v[index + 1] = new_v[index + 1] + value_m[index][new_v[0]]
            # increase item count
            new_v[0] = new_v[0] + 1
            # reset visit count
            new_v[3] = 0
            number_of_states = number_of_states + 1
            # tree_stack.append(new_v)
            if pruning is False:
                tree_stack.append(new_v)
            elif remove_duplicate_states(all_states, new_v) is False:
                tree_stack.append(new_v)
    print(f'number of states calculated when pruning was: {pruning}, num of states: {number_of_states}')


# ------------------------ Q2 ------------------------------
def remove_duplicate_states(states: dict[int, set], curr: list):
    """
    check that state isnt in a given states list
    >>> states = {1: set(),0: set()}
    >>> states[1].add(tuple([0, 0]))
    >>> states[0].add(tuple([0, 0]))
    >>> remove_duplicate_states(states, [0, 0, 1, 0])
    False


    add a new item number state classifier
    >>> states = {1: set()}
    >>> states[1].add(tuple([0, 0]))
    >>> remove_duplicate_states(states, [0, 0, 1, 0])
    False


    >>> states = {1: set(),0: set()}
    >>> states[1].add(tuple([0, 0]))
    >>> states[0].add(tuple([0, 0]))
    >>> remove_duplicate_states(states, [0, 0, 0, 0])
    True

    check if a state was already visited
    :param states: all unique states
    :param curr:
    :return:
    """
    # check if key already exist
    if states.keys().__contains__(curr[0]):
        # if div already calculated from in different branch then stop the calculation
        if states.get(curr[0]).__contains__(tuple(curr[1:len(curr) - 1])):
            # print(f'state already calculated for this branch curr:{curr}')
            return True
        else:
            # this is a new unique state for this item divide add to divide
            # print(f'not in set curr:{curr}')
            states.get(curr[0]).add(tuple(curr[1:len(curr) - 1]))
    else:
        # create new key in dictionary
        states[curr[0]] = set()
        states[curr[0]].add(tuple(curr[1:len(curr) - 1]))
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
