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


def check_win(board, player):
    if player == 1:
        for space in board:
            if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
                return True
            elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
                return True
            elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
                return True
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
                return True
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
                return True
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
                return True
            else:
                return False
    if player == 2:
        for space in board:
            if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
                return True
            elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
                return True
            elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
                return True
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
                return True
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
                return True
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
                return True
            else:
                return False


def check_tie(board):
    spread = [str(inner_list) for inner_list in board]
    spread = "".join(spread)
    return " " not in spread


def play():
    counter = 1
    while True:
        if counter % 2 == 0:
            player = 2
        else:
            player = 1
        display_board(grid)
        player_input(player)
        if check_win(grid, player) == True:
            print(f"Player{player} wins!")
            display_board()
            break
        else:
            if check_tie(grid) == True:
                print("It is a tie!")
                break
        counter += 1


play()
