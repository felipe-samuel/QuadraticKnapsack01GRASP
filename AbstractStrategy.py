import abc

class AbstractStrategy(metaclass = abc.ABCMeta):
    """docstring for AbstractStrategy."""

    @abc.abstractmethod
    def objectiveFunction(self, solution):
        return

    @abc.abstractmethod
    def compareSolution(self, solution1, solution2):
        return

    @abc.abstractmethod
    def randomSolution(self):
        return

    @abc.abstractmethod
    def construction(self):
        return

    @abc.abstractmethod
    def improvement(self, solution):
        return
