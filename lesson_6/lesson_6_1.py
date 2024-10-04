# ДЗ 6.1. Рахування унікальних символів в строці
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True,
# інакше - False.
# Строку отримати за допомогою функції input()

word = input("Plese enter word: ")
uniq_symbols = set()

for symbol in word:
    uniq_symbols.add(symbol)

print(len(uniq_symbols) >= 10)