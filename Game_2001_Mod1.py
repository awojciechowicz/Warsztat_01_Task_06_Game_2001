from random import randint, shuffle
from roll_the_dices import throw_the_dice, POSSIBLE_DICES


def roll_the_dice(points, first_roll, second_roll):
    suma = 0
    if points == 0:
        suma = throw_the_dice(first_roll)
        suma = suma + throw_the_dice(second_roll)
        # print(suma)
        points = points + suma
    else:
        suma = suma + throw_the_dice(first_roll)
        suma = suma + throw_the_dice(second_roll)
        if suma == 7:
            points = points // 7
        if suma == 11:
            points = points * 11
        else:
            points = points + suma
        # print(suma)
    return points



def game_2001():
    user_points = 0
    computer_points = 0

    first_roll = str(input("Choose a dice:"))
    second_roll = str(input("Choose a dice:"))
    # first_roll = "D3"
    # second_roll = "D6"
    user_points += roll_the_dice(user_points, first_roll, second_roll)
    computer_points += roll_the_dice(computer_points, POSSIBLE_DICES[randint(0,len(POSSIBLE_DICES)-1)], POSSIBLE_DICES[randint(0,len(POSSIBLE_DICES)-1)])

    while user_points < 2001 and computer_points < 2001:
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        first_roll = str(input("Choose a dice:"))
        second_roll = str(input("Choose a dice:"))
        user_points += roll_the_dice(user_points, first_roll, second_roll)
        computer_points += roll_the_dice(computer_points, POSSIBLE_DICES[randint(0,len(POSSIBLE_DICES)-1)], POSSIBLE_DICES[randint(0,len(POSSIBLE_DICES)-1)])

    if user_points > computer_points:
        print(f"You win with result {user_points} : {computer_points}")
    elif user_points < computer_points:
        print(f"You lose with result {user_points} : {computer_points}")
    else:
        print("Draw")
game_2001()