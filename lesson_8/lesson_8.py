lst1: list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def calculate_sum(text: list):
    for word in [el.split(",") for el in text]:
        try:
            print(sum([int(el) for el in word]))
        except ValueError:
            print("Не можу це зробити")


calculate_sum(lst1)
