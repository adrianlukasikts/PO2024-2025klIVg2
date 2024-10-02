from chess.bishop import Bishop
from chess.colors import Color
from chess.field import Field
from chess.king import King
from chess.knight import Knight
from chess.pawn import Pawn
from chess.queen import Queen
from chess.rook import Rook


class InvalidMoveException(Exception):
    pass


class Board:
    def __init__(self):
        white_pieces = [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()]
        black_pieces = [Rook(Color.BLACK), Knight(Color.BLACK), Bishop(Color.BLACK), Queen(Color.BLACK), King(Color.BLACK), Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)]
        self.grid = [
            [
                Field(white_piece),
                Field(Pawn()),
                *[Field() for _ in range(4)],
                Field(Pawn(Color.BLACK)),
                Field(black_piece)
            ] for white_piece, black_piece in zip(white_pieces, black_pieces)
        ]
        self.color_current_player = Color.WHITE
        self.move_counter = 1
        self.game_is_finished = False

    def print_board(self):
        for row in range(7, -1, -1):
            print(row + 1, end=" ")

            for column in range(8):
                print(self.grid[column][row].get_piece_name(), end=" ")
            print()
        print("  ", end=" ")
        for i in range(8):
            print(chr(ord("A") + i), end="    ")
        print()
    def is_valid_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        our_piece = self.grid[x1][y1].piece
        move_destination = self.grid[x2][y2]
        if not our_piece:
            return False
        if self.color_current_player != our_piece.color:
            return False
        if move_destination.piece and move_destination.piece.color == our_piece.color:
            return False
        moves = our_piece.get_moves_set(x1, y1)
        if not (x2, y2) in moves:
            return False
        moves_between = our_piece.get_moves_between(x1, y1, x2, y2)
        for i, j in moves_between:
            if self.grid[i][j].piece is not None:
                return False
        return True

    def make_move(self, x1: int, y1: int, x2: int, y2: int):
        if self.is_valid_move(x1, y1, x2, y2):
            self.grid[x2][y2].piece = self.grid[x1][y1].piece
            self.grid[x1][y1].piece = None
            self.color_current_player = Color(self.color_current_player.value * -1)
            self.move_counter += 1
        else:
            raise InvalidMoveException()

    def get_pos_from_notation(self, notation:str):
        letter = notation[0] # FIXME
        y = int(notation[1]) - 1
        x = ord(letter) - ord("A")
        return x, y



board = Board()
board.print_board()



try:
    # board.make_move(1, 1, 1, 2)
    # board.print_board()
    # board.make_move(0, 6, 0, 5)
    # board.print_board()
    # board.make_move(1,2,1,3)
    # board.print_board()
    # board.make_move(1,3,1,4)
    # board.print_board()
    # board.make_move(1,4, 0, 5)
    # board.make_move(*board.get_pos_from_notation("E2"),*board.get_pos_from_notation("E4"))
    # board.print_board()
    # board.make_move(3,6,3,4)
    # board.print_board()
    # board.make_move(4,3,3,4)
    # board.print_board()

    while not board.game_is_finished:
        board.print_board()
        position = input("Podaj nastepny ruch: ")
        position_split = position.split(" ")
        movement = board.get_pos_from_notation(position_split[0])
        movement_two = board.get_pos_from_notation(position_split[1])
        board.make_move(*movement, *movement_two)
except InvalidMoveException:

    print(f"Niepoprawny ruch nr: {board.move_counter}" )
