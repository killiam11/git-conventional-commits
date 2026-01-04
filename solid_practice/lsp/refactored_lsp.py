from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def area(self) -> int:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side
    
    def area(self) -> int:
        return self.side * self.side
    