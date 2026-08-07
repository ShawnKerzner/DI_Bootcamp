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
        while True:
            raw_row = (input("Enter row: "))
            try:
                select_row = int(raw_row)
            except ValueError:
                print("Error: Input must an integer between the values 0 - 2.")
                continue
            if len(raw_row) > 1:
                print("Error: Input must be a single space")
                continue
            if select_row not in (0, 1, 2):
                print("Error: Input must an integer between the values 0 - 2.")
                continue
            break
        while True:
            raw_column = (input("Enter column: "))
            try:
                select_column = int(raw_column)
            except ValueError:
                print("Error: Input must an integer between the values 0 - 2.")
                continue
            if len(raw_column) > 1:
                print("Error: Input must be a single space")
                continue
            if select_column not in (0, 1, 2):
                print("Error: Input must an integer between the values 0 - 2.")
                continue
            break
        marked = grid[(select_row)][(select_column)]
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
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                return True
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
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
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                return True
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                return True
            else:
                return False


def check_tie(board):
    for inner_list in board:
        if " " in inner_list:
            return False
    return True


def play():
    counter = 1
    while True:
        if counter % 2 == 0:
            player = 2
            print("Player 2's turn")
        else:
            player = 1
            print("Player 1's turn")
        display_board(grid)
        player_input(player)
        if check_win(grid, player) == True:
            print(f"Player{player} wins!")
            display_board(grid)
            break
        else:
            if check_tie(grid) == True:
                print("It is a tie!")
                break
        counter += 1


play()
