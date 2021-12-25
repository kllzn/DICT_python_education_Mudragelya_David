def game():
    cells = list(input("Enter cells:"))
    print(f"""
    {"-" * 9}
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    {"-" * 9}
    """)
    result = []
    if cells.count("X") - cells.count("O") >= 2 or cells.count("O") - cells.count("X") >= 2:
        print("Impossible")
    if cells[0] == cells[1] == cells[2] != "-":
        result.append(cells[0])
    if cells[3] == cells[4] == cells[5] != "-":
        result.append(cells[3])
    if cells[6] == cells[7] == cells[8] != "-":
        result.append(cells[6])
    if cells[0] == cells[3] == cells[6] != "-":
        result.append(cells[0])
    if cells[1] == cells[4] == cells[7] != "-":
        result.append(cells[1])
    if cells[2] == cells[5] == cells[8] != "-":
        result.append(cells[2])
    if len(result) >= 2:
        print("Impossible")
    if len(result) == 1:
        print(f"{result[0]} wins!")
    if '_' in cells and len(result) == 0:
        print("Game not finished")
    elif '_' not in cells and len(result) == 0:
        print("Draw")


game()
