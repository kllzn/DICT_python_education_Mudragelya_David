cells = list(input("Enter cells: "))
win = 0


def board():
    print(f"""
    |{cells[0]}{cells[1]}{cells[2]}|
    |{cells[3]}{cells[4]}{cells[5]}|
    |{cells[6]}{cells[7]}{cells[8]}|
    """)


board()


def game():
    result = []
    global win
    if cells.count("X") - cells.count("O") >= 2 or cells.count("O") - cells.count("X") >= 2:
        return "Impossible"
    if cells[0] == cells[1] == cells[2] != "-":
        result.append(cells[0])
        win += 1
    if cells[3] == cells[4] == cells[5] != "-":
        result.append(cells[3])
        win += 1
    if cells[6] == cells[7] == cells[8] != "-":
        result.append(cells[6])
        win += 1
    if cells[0] == cells[3] == cells[6] != "-":
        result.append(cells[0])
        win += 1
    if cells[1] == cells[4] == cells[7] != "-":
        result.append(cells[1])
        win += 1
    if cells[2] == cells[5] == cells[8] != "-":
        result.append(cells[2])
        win += 1
    if len(result) >= 2:
        return "Impossible"
    if len(result) == 1:
        return result[0] + " wins!"
    if '_' in cells and len(result) == 0:
        return "Game not finished"
    elif '_' not in cells and len(result) == 0:
        return "Draw"


def turn():
    while True:
        coords = list(input("Enter the coordinates:"))
        x, y = str(coords[2]), str(coords[0])
        if x.isalpha() or y.isalpha() or x == "" or y == "":
            print("You should enter numbers!")
        if int(x) not in range(3) or int(y) not in range(3):
            print('Coordinates should be from 1 to 3!')
        if y == "1":
            if x == "1":
                if cells[0] != "X" and cells[0] != "O":
                    cells[0] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "2":
                if cells[1] != "X" and cells[1] != "O":
                    cells[1] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "3":
                if cells[2] != "X" and cells[2] != "O":
                    cells[2] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
        if y == "2":
            if x == "1":
                if cells[3] != "X" and cells[3] != "O":
                    cells[3] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "2":
                if cells[4] != "X" and cells[4] != "O":
                    cells[4] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "3":
                if cells[5] != "X" and cells[5] != "O":
                    cells[5] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
        if y == "3":
            if x == "1":
                if cells[6] != "X" and cells[6] != "O":
                    cells[6] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "2":
                if cells[7] != "X" and cells[7] != "O":
                    cells[7] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            elif x == "3":
                if cells[8] != "X" and cells[8] != "O":
                    cells[8] = "X"
                else:
                    print("This cell is occupied! Choose another one!")
        board()
        game()
        if win == 1:
            break
    board()
    print(game())


turn()
