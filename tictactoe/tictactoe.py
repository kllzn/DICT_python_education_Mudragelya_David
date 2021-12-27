import random

cells = {11: "_", 12: "_", 13: "_",
         21: "_", 22: "_", 23: "_",
         31: "_", 32: "_", 33: "_"}
verify = 0


def create_board():
    print(f"""{'-' * 9}
| {cells[11]} {cells[12]} {cells[13]} |
| {cells[21]} {cells[22]} {cells[23]} |
| {cells[31]} {cells[32]} {cells[33]} |
{'-' * 9}
""")


def winner():
    global verify
    result = []
    list_cells = [value for value in cells.values()]
    underline_amount = list_cells.count("_")
    if cells[11] == cells[22] == cells[33] != "_":
        result.append(cells[11])
    if cells[13] == cells[22] == cells[31] != "_":
        result.append(cells[13])
    if cells[11] == cells[12] == cells[13] != "_":
        result.append(cells[11])
    if cells[21] == cells[22] == cells[23] != "_":
        result.append(cells[21])
    if cells[31] == cells[32] == cells[33] != "_":
        result.append(cells[31])
    if cells[11] == cells[21] == cells[31] != "_":
        result.append(cells[11])
    if cells[12] == cells[22] == cells[32] != "_":
        result.append(cells[12])
    if cells[13] == cells[23] == cells[33] != "_":
        result.append(cells[13])
    if result.count('X') >= 2:
        result.remove('X')
    if result.count('O') >= 2:
        result.remove('O')
    if len(result) == 1:
        verify += 1
        print(f"{result[0]} wins!")
    if "_" not in cells.values():
        if underline_amount == 0:
            verify += 1
            print("Draw!")


def turn_x():
    global verify
    while verify == 0:
        coords = list(input("Enter the coordinates:"))
        if len(coords) == 2:
            if 48 <= ord(coords[0]) <= 57 or 48 <= ord(coords[1]) <= 57:
                if int(coords[0]) in range(1, 4) and int(coords[1]) in range(1, 4):
                    numbers = int("".join(str(i) for i in coords))
                    if cells[numbers] == "_":
                        cells[numbers] = "X"
                        create_board()
                        winner()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        elif len(coords) == 3:
            coords.remove(" ")
            if 48 <= ord(coords[0]) <= 57 or 48 <= ord(coords[1]) <= 57:
                if int(coords[0]) in range(1, 4) and int(coords[1]) in range(1, 4):
                    numbers = int("".join(str(i) for i in coords))
                    if cells[numbers] == "_":
                        cells[numbers] = "X"
                        create_board()
                        winner()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")


def turn_o():
    global verify
    while verify == 0:
        coords = list(input("Enter the coordinates:"))
        if len(coords) == 2:
            if 48 <= ord(coords[0]) <= 57 or 48 <= ord(coords[1]) <= 57:
                if int(coords[0]) in range(1, 4) and int(coords[1]) in range(1, 4):
                    numbers = int("".join(str(i) for i in coords))
                    if cells[numbers] == "_":
                        cells[numbers] = "O"
                        create_board()
                        winner()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        elif len(coords) == 3:
            coords.remove(" ")
            if 48 <= ord(coords[0]) <= 57 or 48 <= ord(coords[1]) <= 57:
                if int(coords[0]) in range(1, 4) and int(coords[1]) in range(1, 4):
                    numbers = int("".join(str(i) for i in coords))
                    if cells[numbers] == "_":
                        cells[numbers] = "O"
                        create_board()
                        winner()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")


create_board()

first_turn = random.randint(1,2)
while verify != 1:
    if first_turn == 1:
        turn_x()
        turn_o()
    else:
        turn_o()
        turn_x()

