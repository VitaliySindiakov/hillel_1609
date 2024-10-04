# ДЗ 6.1. Рахування унікальних символів в строці
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True,
# інакше - False.
# Строку отримати за допомогою функції input()

word = input("Plese enter word: ")
uniq_symbols: dict = {}

for symbol in word:
    symbol = symbol.lower()
    if symbol in uniq_symbols.keys():
        uniq_symbols[symbol] = uniq_symbols.get(symbol) + 1
    else:
        uniq_symbols[symbol] = 1

print(uniq_symbols)

is_uniq_present = False
for value in uniq_symbols.values():
    if value >= 10:
        is_uniq_present = True
        break

print(is_uniq_present)