"""
Bad LSP example.

Square inherits from Rectangle but changes
the expected behavior of setters.
"""

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, width: int) -> None:
        self.width = width
    
    def set_height(self, height: int) -> None:
        self.height = height
    
    def area(self) -> int:
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width
    
    def set_height(self, height: int) -> None:
        self.width = height
        self.height = height
        