class TicTacTowBoard:

    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_game_board(self):
        """
        Print the TicTacToe board game with the actual game configuration
        :rtype: console print
        """
        print("    0     1     2   ")
        print(f"0   {self.game[0][0]}  |  {self.game[0][1]}  |  {self.game[0][2]}")
        print("  -----------------")
        print(f"1   {self.game[1][0]}  |  {self.game[1][1]}  |  {self.game[1][2]}")
        print("  -----------------")
        print(f"2   {self.game[2][0]}  |  {self.game[2][1]}  |  {self.game[2][2]}")

    def place_game_piece(self, piece: str, row: int, col: int) -> bool:
        """
        Places a specific piece in a row and column of the board
        :param piece: any one character string
        :param row: integer from 0 to 2
        :param col: integer from 0 to 2
        :return: Boolean if success
        """
        if self.is_valid_play(row, col):
            self.game[row][col] = piece
            return True
        else:
            return False

    def is_valid_play(self, row: int, column: int) -> bool:
        """
        Validates if the selected row and column are empty and the values are within 0 and 2
        :param row: integer from 0 to 2
        :param column: integer from 0 to 2
        :return: Boolean if success
        """
        if not (0 <= row <= 2 and 0 <= column <= 2):
            return False
        if self.game[row][column] == " ":
            return True
        else:
            return False

    def check_result(self) -> str:
        """
        Checks if any row, column or diagonal have the same piece and if there are no more blank spaces
        :return: Piece if any player wins, "Draw" if no more spaces exist in the board
        """
        result = ""
        # Check rows:
        for row in range(self.rows):
            if self.game[row][0] == self.game[row][1] == self.game[row][2] != " ":
                result = self.game[row][0]
        # Check columns:
        for column in range(self.columns):
            if self.game[0][column] == self.game[1][column] == self.game[2][column] != " ":
                result = self.game[0][column]
        # Check diagonals:
        if self.game[0][0] == self.game[1][1] == self.game[2][2] != " ":
            result = self.game[0][0]
        if self.game[2][0] == self.game[1][1] == self.game[0][2] != " ":
            result = self.game[0][0]
        # Check draw:
        if not any(" " in sl for sl in self.game):
            result = "Draw"

        return result
