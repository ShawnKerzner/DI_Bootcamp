grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def display_board(grid):
    print(f"TIC TAC TOE")
    print("*" * 17)
    print(f"*   {grid[0][0]} | {grid[0][1]} | {grid[0][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {grid[1][0]} | {grid[1][1]} | {grid[1][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {grid[2][0]} | {grid[2][1]} | {grid[2][2]}   *")
    print("*" * 17)


def player_input(player):
    while True:
        select_row = int(input("Enter row: "))
        select_column = int(input("Enter column: "))
        marked = grid[select_row][select_column]
        if marked != " ":
            print("This spot is already taken")
        else:
            grid[select_row][select_column] = "X" if player == 1 else "O"
            break


player_input(1)
display_board(grid)
