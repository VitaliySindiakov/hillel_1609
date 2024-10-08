# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            print(f"value {result} greater than 25")
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two(first: int, second: int):
    return first + second


print(sum_of_two(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)


print(arithmetic_mean([1, 2, 3, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_string(text: str) -> str:
    return text[::-1]


print(revers_string("Hello world"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def get_longest_word(words: list) -> str:
    max_len_word = ""
    for word in words:
        if len(word) > len(max_len_word):
            max_len_word = word
    return max_len_word


print(get_longest_word(["Car", "Bycycle", "Helicopter", "Train"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# ___ LESSON 5.2 ___
people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

def check_person_age_by_index(people: list) -> None:
    for person in people:
        first_name, last_name, age, position, location = person
        if age >= 30:
            print(f"Person {person} is 30 or older")
        else:
            print(f"Person {person} is younger 30")


check_person_age_by_index([people_records[0], people_records[2], people_records[4]])


# task 8
# ___ LESSON 5.1 ___
car_data: dict = {
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}


def get_cars_by_criteria(criteria: tuple) -> dict:
    filtered_cars = {}
    for key, value in car_data.items():
        color, year, engine_volume, car_type, price = value
        cr_year, cr_engine_volume, cr_price = criteria
        if year >= cr_year and engine_volume >= cr_engine_volume and price <= cr_price:
            print(f"Criteria match for car {key} {value}")
            filtered_cars[key] = value
    return filtered_cars


print(get_cars_by_criteria((2017, 1.6, 36000)))


# task 9
# ___ LESSON 6.3 ___
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


def get_str_list(lst1: list) -> list:
    return [el for el in lst1 if isinstance(el, str)]


print(get_str_list(lst1))


# task 10
# ___ LESSON 6.4 ___

def even_numbers_sum(numbers: list) -> int:
    return sum([k for k in numbers if k % 2 == 0])


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(even_numbers_sum(lst1))
