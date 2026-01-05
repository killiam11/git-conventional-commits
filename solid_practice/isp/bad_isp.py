from abc import ABC, abstractmethod

"""
Bad ISP example.

A fat interface forces classes to implement
methods they do not need.
"""

class Worker(ABC):
    @abstractmethod
    def work(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass


class HumanWorker(Worker):
    def work(self) -> None:
        print("Human is working")

    def eat(self) -> None:
        print("Human is eating")


class RobotWorker(Worker):
    def work(self) -> None:
        print("Robot is working")

    def eat(self) -> None:
        raise NotImplementedError("Robots do not eat")
