grid = [[" ", " ", " "], [" ", " ", ""], [" ", " ", " "]]


def display_board(grid):
    print(f"TIC TAC TOE")
    print("*" * 17)
    print(f"*   {grid[0][0]} | {grid[0][1]} | {grid[0][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {grid[1][0]} | {grid[1][1]} | {grid[1][2]}    *")
    print("*  ---|---|---  *")
    print(f"*   {grid[2][0]} | {grid[2][1]} | {grid[2][2]}   *")
    print("*" * 17)


display_board(grid)
