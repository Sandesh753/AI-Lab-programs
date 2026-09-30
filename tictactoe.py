# Tic-Tac-Toe

board = [" "] * 9


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner():
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True

    return False


def play_game():
    player = "X"

    for turn in range(9):
        display_board()

        position = int(input(
            f"Player {player}, enter position (1-9): "
            )) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move! Try again.")
            continue

        board[position] = player

        if check_winner():
            display_board()
            print(f"Player {player} wins!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    display_board()
    print("It's a draw!")


play_game()