import random


def rand_dice() -> int:
    return random.randint(1, 6)


def calculate_points(dices: list[int]) -> int:
    dices.sort()
    counter = 1
    current_dice = dices[0]
    result = 0
    for dice in dices[1:]:
        if current_dice == dice:
            counter += 1
        else:
            if counter >= 2:
                result += (counter * current_dice)
            current_dice = dice
            counter = 1
    if counter >= 2:
        result += (counter * current_dice)
    return result


dice_number = int(input("Ile kostek chcesz rzucic?(3 - 10)\n"))
while not 3 <= dice_number <= 10:
    dice_number = int(input("Ile kostek chcesz rzucic?(3 - 10)\n"))

is_again = "t"
while is_again == "t":
    dices = [rand_dice() for _ in range(dice_number)]
    for i in range(len(dices)):
        print(f"Kostka {i + 1}: {dices[i]}")
    print(f"Liczba uzyskanych punktów {calculate_points(dices)}")
    is_again = input("Jeszcze raz? (t/n)\n")
