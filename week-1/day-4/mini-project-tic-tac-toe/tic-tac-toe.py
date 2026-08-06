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


def check_win(board, player):
    if player == 1:
        for space in board:
            if board[0][0] == "X" and board[0][1] == "X" and board[0][2]:
                return True
            elif board[1][0] == "X" and board[1][1] == "X" and board[1][2]:
                return True
            elif board[2][0] == "X" and board[2][1] == "X" and board[2][2]:
                return True
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][0]:
                return True
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][1]:
                return True
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][2]:
                return True
            else:
                return False
    if player == 2:
        for space in board:
            if board[0][0] == "O" and board[0][1] == "O" and board[0][2]:
                return True
            elif board[1][0] == "O" and board[1][1] == "O" and board[1][2]:
                return True
            elif board[2][0] == "O" and board[2][1] == "O" and board[2][2]:
                return True
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][0]:
                return True
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][1]:
                return True
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][2]:
                return True
            else:
                return False
