from abc import ABC, abstractmethod
import math
import pytest


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} Area = {self.get_area()} Peritemeter = {self.get_perimeter()}"


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def get_perimeter(self):
        return self.__a + self.__b + self.__c


class Quadrate(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return self.__side * 4


rectangle = Rectangle(width=4, height=6)
triangle = Triangle(a=3, b=4, c=5)
quadrate = Quadrate(side=4)


@pytest.mark.parametrize("actual_area, expected_area", [
    (rectangle.get_area(), 24),
    (triangle.get_area(), 6),
    (quadrate.get_area(), 16)
])
def test_figures_area(actual_area, expected_area):
    assert actual_area == expected_area


@pytest.mark.parametrize("actual_perimeter, expected_perimeter", [
    (rectangle.get_perimeter(), 20),
    (triangle.get_perimeter(), 12),
    (quadrate.get_perimeter(), 16)
])
def test_figures_perimeter(actual_perimeter, expected_perimeter):
    assert actual_perimeter == expected_perimeter
