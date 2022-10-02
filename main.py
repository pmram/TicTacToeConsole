from tictactowboard import TicTacTowBoard

board = TicTacTowBoard()


def get_player_move(active_player: int) -> (int, int):
    """
    Function that asks player for the play coordinates and converts them into an integer tuple (row, col)
    :param active_player: Integer with the player number (1 or 2)
    :return: Tuple with two integers, if error it returns invalid coordinates tuple (-1, -1)
    """
    if active_player == 1:
        player_name = "Player 1"
    else:
        player_name = "Player 2"
    user_move = input(f"{player_name} select the position want to play using the scheme row, column? (ex:. 1,2) \n")
    try:
        player_row = int(user_move.split(",")[0])
        player_column = int(user_move.split(",")[1])
    except ValueError:
        return -1, -1
    return player_row, player_column


def print_result(game_result: str):
    """
    Prints in the console the strings of the result
    :param game_result: String with the piece of the player or the string "Drow"
    """
    if game_result == "X":
        print("Player 1 won the game!")
    elif game_result == "O":
        print("Player 2 won the game!")
    else:
        print("There is a draw! Try again!")


# Play game
result = ""
player = 1
game_piece = "X"
print("Player 1 with piece 'X' and player 2 with piece 'O'")
board.print_game_board()
while result == "":
    valid_play = False
    while not valid_play:
        player_move = get_player_move(player)
        if board.place_game_piece(game_piece, player_move[0], player_move[1]):
            valid_play = True
            # Change player
            if player == 1:
                player = 2
                game_piece = "O"
            else:
                player = 1
                game_piece = "X"
        else:
            print("It is not valid to play in the selected coordinates. Try again!\n")
        result = board.check_result()
    board.print_game_board()

print_result(result)