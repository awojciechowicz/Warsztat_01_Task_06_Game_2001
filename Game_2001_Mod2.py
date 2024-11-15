from random import randint, shuffle
from roll_the_dices import throw_the_dice, POSSIBLE_DICES
from flask import Flask, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        html = """
        <form method="POST" action="/">
            <select name="first_dice">
                <option value="D6">D6</option>
                <option value="D4">D4</option>
                <option value="D3">D3</option>
                <option value="D8">D8</option>
                <option value="D10">D10</option>
                <option value="D12">D12</option>
                <option value="D20">D20</option>
                <option value="D100">D100</option>
            </select>
            <select name="second_dice">
                <option value="D6">D6</option>
                <option value="D4">D4</option>
                <option value="D3">D3</option>
                <option value="D8">D8</option>
                <option value="D10">D10</option>
                <option value="D12">D12</option>
                <option value="D20">D20</option>
                <option value="D100">D100</option>
            </select>
            <input type="hidden" name="user_points" value="0">
            <input type="hidden" name="computer_points" value="0">
            <input type="submit" value="Submit">
        </form>
        """
        return html
    if request.method == 'POST':
        user_points = int(request.form['user_points'])
        computer_points = int(request.form['computer_points'])
        first_roll = str(request.form['first_dice'])
        second_roll = str(request.form['second_dice'])
        user_points += roll_the_dice(user_points, first_roll, second_roll)
        computer_points += roll_the_dice(computer_points, POSSIBLE_DICES[randint(0, len(POSSIBLE_DICES) - 1)],
                                         POSSIBLE_DICES[randint(0, len(POSSIBLE_DICES) - 1)])
        if user_points < 2001 and computer_points < 2001:
            html = f"""
            <form method="POST" action="/">
                <select name="first_dice">
                    <option value="D6">D6</option>
                    <option value="D4">D4</option>
                    <option value="D3">D3</option>
                    <option value="D8">D8</option>
                    <option value="D10">D10</option>
                    <option value="D12">D12</option>
                    <option value="D20">D20</option>
                    <option value="D100">D100</option>
                </select>
                <select name="second_dice">
                    <option value="D6">D6</option>
                    <option value="D4">D4</option>
                    <option value="D3">D3</option>
                    <option value="D8">D8</option>
                    <option value="D10">D10</option>
                    <option value="D12">D12</option>
                    <option value="D20">D20</option>
                    <option value="D100">D100</option>
                </select>
                <input type="hidden" name="user_points" value={user_points}>
                <input type="hidden" name="computer_points" value={computer_points}>
                <input type="submit" value="Submit"><br>
                User points: {user_points}<br>
                Computer points: {computer_points}
            </form>
            """
        elif user_points > computer_points:
            html = f"""
            You win with result {user_points} : {computer_points}
            """
        elif user_points < computer_points:
            html = f"""
            You lose with result {user_points} : {computer_points}
            """
        else:
            html = """
            Draw
            """
        return html


if __name__ == '__main__':
    app.run(debug=True)