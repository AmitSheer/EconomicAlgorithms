from typing import List
import cvxpy


def Nash_budget(
        total: float, subjects: List[str],
        preferences: List[List[str]]
):
    """
    >>> Nash_budget(500, ['a', 'b', 'c', 'd'], [['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['a']])
    Citizen 0 gives 85.07809351327815 to a and  14.921906486721838 to b.
    Citizen 1 gives 85.07809351326448 to a and  14.921906486735514 to c.
    Citizen 2 gives 99.99999253028457 to a and  7.469715425616163e-06 to d.
    Citizen 3 gives 49.99999999997307 to b and  50.00000000002693 to c.
    Citizen 4 gives 100.0 to a.

    """
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

    print_results(allocations, donations, preferences, subjects, utilities)


def print_results(allocations, donations, preferences, subjects, utilities):
    for i in range(len(preferences)):
        to_print = f"Citizen {i} gives "
        sub = []
        for pref in preferences[i]:
            for j in pref:
                sub.append(f"{allocations[subjects.index(j)].value * donations[i] / utilities[i].value} to {j}")
        to_print += sub.__str__().replace('[', '').replace(']', '.').replace(',', ' and ').replace('\'', '')
        print(to_print)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
