# ДЗ 6.2. Цикл “Дочекайся літери”
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    word = input("Plese enter word with 'h': ")
    if 'h' in word or 'H' in word:
        print('letter \'h\' present in the word')
        break
    else:
        print('letter \'h\' not found')