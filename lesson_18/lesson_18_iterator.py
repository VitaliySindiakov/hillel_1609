# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
import pytest


class Revert_Iter():
    def __init__(self, list_to_revert: list):
        self.__current = len(list_to_revert) - 1
        self.__list = list_to_revert

    def __iter__(self):
        return self

    def __next__(self):
        element = self.__list[self.__current]
        self.__current -= 1
        if self.__current < -1:
            raise StopIteration

        return element


class Prime_Iter():
    def __init__(self, max_range: int):
        self.__current = 0
        self.__max_range = max_range

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == self.__max_range:
            raise StopIteration

        while not self._is_prime(self.__current):
            self.__current = self.__current + 1

        temp = self.__current
        self.__current = self.__current + 1
        return temp

    @classmethod
    def _is_prime(self, number):
        if number >= 2:
            if number % 2 == 0:
                return True
        return False


for k in Revert_Iter(["Alex", "Ivan", "Den"]):
    print("name=", k)

for el in Prime_Iter(7):
    print("prime number = ", el)


@pytest.mark.parametrize("expected, actual", [
    (["Alex", "Ivan", "Den"], list(Revert_Iter(["Den", "Ivan", "Alex"])))
])
def test_revert_iter(expected: list, actual: list):
    print("Expected = ", expected)
    print("Actual = ", actual)
    assert expected == actual

@pytest.mark.parametrize("expected, actual", [
    ([2,4,6], list(Prime_Iter(7)))
])
def test_prime_iter(expected: int, actual: int):
    print("Expected = ", expected)
    print("Actual = ", actual)
    assert expected == actual
