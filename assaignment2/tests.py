from unittest import TestCase

from assaignment2.main import Agent, isParetoOptimal, isParetoImprovement

Ami = Agent([1, 2, 3, 4, 5])
Tami = Agent([3, 1, 2, 5, 4])
Rami = Agent([3, 5, 5, 1, 1])
allAgents = [Ami, Tami, Rami]


class Test_with_data(TestCase):

    def test_Pareto_Improvement(self):
        self.assertTrue(isParetoImprovement(allAgents, 2, 1))

    def test_Pareto_Optimal(self):
        results = [True, False, True, True, True]
        for i in range(0, 5):
            print(f'{i}')
            self.assertTrue(isParetoOptimal(allAgents, i, [0, 1, 2, 3, 4]) == results.__getitem__(i))
