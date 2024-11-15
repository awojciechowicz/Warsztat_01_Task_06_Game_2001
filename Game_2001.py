from random import randint


def roll_the_dice(points):
    suma = 0
    if points == 0:
        for _ in range(2):
            suma += randint(1,6)
        print(suma)
        points = points + suma
    else:
        for _ in range(2):
            suma += randint(1,6)
            if suma == 7:
                points = points // 7
            if suma == 11:
                points = points * 11
            else:
                points = points + suma
        print(suma)
    return points



def game_2001():
    user_points = 0
    computer_points = 0

    input("Press ENTER to roll the dice.")
    user_points += roll_the_dice(user_points)
    computer_points += roll_the_dice(computer_points)

    while user_points < 2001 and computer_points < 2001:
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        input("Press ENTER to roll the dice.")
        user_points += roll_the_dice(user_points)
        computer_points += roll_the_dice(computer_points)

    if user_points > computer_points:
        print(f"You win with result {user_points} : {computer_points}")
    elif user_points < computer_points:
        print(f"You lose with result {user_points} : {computer_points}")
    else:
        print("Draw")
game_2001()