from typing import List
import cvxpy
import functools


def Nash_budget(
        total: float, subjects: List[str],
        preferences: List[List[str]]
):
    allocations = cvxpy.Variable(len(subjects))
    donations = [total / len(preferences) for i in range(len(preferences))]
    utilities = []
    for pref in preferences:
        g = allocations[subjects.index(pref[0])]
        for i in range(1, len(pref)):
            g += allocations[subjects.index(pref[i])]
        utilities.append(g)

    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
    positivity_constraints = [v >= 0 for v in allocations]
    sum_constraint = [cvxpy.sum(allocations) == sum(donations)]

    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints=positivity_constraints + sum_constraint)
    problem.solve()

    for i in range(len(preferences)):
        k = 0
        to_print = f"Citizen {i} gives "
        sub = []
        for pref in preferences[i]:
            for j in pref:
                sub.append(f"{allocations[subjects.index(j)].value * donations[i] / utilities[i].value} to {j}")
        to_print += sub.__str__().replace('[', '').replace(']', '.').replace(',', 'and ')
        print(to_print)


if __name__ == '__main__':
    Nash_budget(
        500,
        ['a', 'b', 'c', 'd'],
        [[
            'a', 'b'
        ], [
            'a', 'c'
        ], [
            'a', 'd'
        ], [
            'b', 'c'
        ], [
            'a'
        ]]
    )
    print('ads')
