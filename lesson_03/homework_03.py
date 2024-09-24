alice_in_wonderland: str = ('"Would you tell me, please, which way I ought to go from here?"\n'
                            '"That depends a good deal on where you want to get to," said the Cat.\n'
                            '"I don\'t much care where ——" said Alice.\n'
                            '"Then it doesn\'t matter which way you go," said the Cat.\n'
                            '"—— so long as I get somewhere," Alice added as an explanation.\n'
                            '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_see = 436402
azov_see = 37800
see_sq = black_see * azov_see
print(f"Площа, яку займають Чорне та Азовське моря разом {see_sq} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_warehouses = 375291
first_and_sec_warehouse = 250449
third_warehouse = all_warehouses - first_and_sec_warehouse
sec_and_third_warehouse = 222950
first_warehouse = all_warehouses - sec_and_third_warehouse
second_warehouse = all_warehouses - third_warehouse - first_warehouse
print(f"""
Кількість товарів на:
першому складі {first_warehouse}
другому складі {second_warehouse}
третьому складі {third_warehouse}
""")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
part_price = 1179
full_price = part_price * 18
print(f"Вартість комп’ютера {full_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
b = 9907 % 9
c = 2789 % 5
e = 7128 % 5
f = 19224 % 9


print(f"""Залишок від ділленя
а) {a}             d) {d}
b) {b}             e) {e}
c) {c}             f) {f}
""")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274 * 4
middle_pizza = 218 * 2
juice  = 35 * 4
cake = 350 * 1
water = 21 * 3
order_total = big_pizza + middle_pizza + juice + cake + water

print(f"Для даного замовлення знадобиться {order_total} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_total = 232
page_capacity = 8
required_pages = 232 / 8


print(f"Ігорю знадобиться {int(required_pages)} сторінок,  щоб вклеїти всі фото")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

destination = 1600
required__total_gas = 1600 / 100 * 9
tank_capacity = 48
required_refueling = required__total_gas / tank_capacity


print(f"1) знадобиться {int(required__total_gas)} літрів бензину для такої подорож")
print(f"2) родині необхідно заїхати на заправку {int(required_refueling)} рази під час цієї подорожі")