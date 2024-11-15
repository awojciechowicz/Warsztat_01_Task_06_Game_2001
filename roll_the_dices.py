import random
POSSIBLE_DICES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")

def throw_the_dice(dice_code):
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            multiplikator, modifier = dice_code.split(dice)
            dice_value = int(dice[1:])
            break
    else:
        print("Wrong input!")

    try:
        if multiplikator != "":
            multiplikator = int(multiplikator)
        else:
            multiplikator = 1
    except ValueError:
        print("Wrong input!")
        return None

    try:
        if modifier != "":
            modifier = int(modifier)
        else:
            modifier = 0
    except ValueError:
        print("Wrong input!")
        return None

    sum = 0
    for _ in range(multiplikator):
        sum += random.randint(1, dice_value)
    sum = sum + modifier
    return sum





# print(throw_the_dice("2D10+10"))
print(throw_the_dice("D6"))
# print(throw_the_dice("2D3"))
# print(throw_the_dice("D12-1"))
# print(throw_the_dice("DD34"))
# print(throw_the_dice("4-3D6"))