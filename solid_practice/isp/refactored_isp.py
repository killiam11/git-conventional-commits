from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self) -> None:
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> None:
        pass


class HumanWorker(Workable, Eatable):
    def work(self) -> None:
        print("Human is working")

    def eat(self) -> None:
        print("Human is eating")


class RobotWorker(Workable):
    def work(self) -> None:
        print("Robot is working")
