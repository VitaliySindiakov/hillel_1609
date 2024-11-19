# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = 10
for number in even_numbers(n):
    print(number)


def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a = b
        b = a + b

n = 20
for number in fibonacci_sequence(n):
    print(number)