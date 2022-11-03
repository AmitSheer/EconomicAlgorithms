from unittest import TestCase

from assaignment2.main import Agent, isParetoOptimal

Ami = Agent([1, 2, 3, 4, 5])
Tami = Agent([3, 1, 2, 5, 4])
Rami = Agent([3, 5, 5, 1, 1])
allAgents = [Ami, Tami, Rami]


class Test_with_data(TestCase):

    def test_(self):
        self.assertTrue(isParetoOptimal(allAgents, 2, 1))
