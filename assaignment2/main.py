class Agent:
    def __init__(self, values: list[int]):
        self.values = values

    def value(self, option: int) -> float:
        """
        INPUT:  the input of an option
        OUTPUT: the value of the option to the agent
        """
        return self.values.__getitem__(option)


def isParetoImprovement(agents: list[Agent], option1: int, option2: int) -> bool:
    """
    checks if an one option is a Pareto improvement on another option
    :param agents: list of agents to check the options on
    :param option1:
    :param option2:
    :return: True if the option1 is better than option2, otherwise return False
    """
    same = True
    agent_values = 0
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            return False
    # this addition to handle cases where the two option are the same so they
    # aren't any better than the other ones
        elif agent.value(option1) == agent.value(option2):
            agent_values = agent_values+1
    if agent_values == len(agents):
        return False
    # end of addition
    return True


def isParetoOptimal(agents: list[Agent], option: int, options: list[int]) -> bool:
    """
    checks if an one option is a Pareto Optimal to all other options
    :param agents: list of agents to check the options on
    :param option: to check for optimality
    :param options: to compare to
    :return: True if the option is better than all other options, otherwise return False
    """
    for op in options:
        if option != op:
            if isParetoImprovement(agents, op, option) is True:
                return False
    return True


if __name__ == '__main__':
    Ami = Agent([1, 2, 3, 4, 5])
    Tami = Agent([3, 1, 2, 5, 4])
    Rami = Agent([3, 5, 5, 1, 1])
