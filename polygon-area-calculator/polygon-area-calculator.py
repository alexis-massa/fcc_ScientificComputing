import math


class Rectangle:
    height: int
    width: int

    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width

    def set_height(self, height: int) -> int:
        self.height = height

    def set_width(self, width: int) -> int:
        self.width = width

    def get_area(self) -> float:
        """
        Get are of Rectangle

        Returns:
            float: The area
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Get perimeter of Rectangle

        Returns:
            int: perimeter
        """
        return 2 * self.height + 2 * self.width

    def get_diagonal(self) -> float:
        """
        Get diagonal height of Rectangle

        Returns:
            float: Diagonal height
        """
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        """
        Returns a string that represent the Rectangle with width * and height lines

        Returns:
            str: The string representation of the Rectangle with '*' character
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return f'{"*" * self.width}\n' * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        """
        Returns the number of times `shape` can fit in the Rectangle

        Args:
            shape (Rectangle): The shape to fit in

        Returns:
            int: The number of times the shame fits
        """
        return math.floor(self.width / shape.width) * math.floor(
            self.height / shape.height
        )

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side: int):
        """
        Set side of square (both height and width)

        Args:
            side (int): The wanted side legnth
        """
        self.height = side
        self.width = side

    def set_height(self, height: int):
        """
        Set height of square (oth height and width)

        Args:
            height (int): The wanted height
        """
        self.set_side(height)

    def set_width(self, width: int):
        """
        Set width of square (oth height and width)

        Args:
            height (int): The wanted width
        """

        self.set_side(width)

    def __str__(self):
        return f"{type(self).__name__}(side={self.height})"


# Usage example
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
