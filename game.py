# Game logic (turns, promotion, capturing)
from board import Board
from pieces import Pawn, Lance, Knight, Silver, Gold, King, Bishop, Rook


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 1
        self.setup_board()

    def setup_board(self):
        """Initialize board with standard Shogi setup."""
        for col in range(9):
            self.board.place_piece(Pawn(1), (6, col)) # Player 1 Pawns
            self.board.place_piece(Pawn(-1), (2, col)) # Player 2 Pawns

            # Lances
            self.board.place_piece(Lance(1), (8, 0)) # Player 1 Lance   
            self.board.place_piece(Lance(1), (8, 8))
            self.board.place_piece(Lance(-1), (0, 0)) # Player 2 Lance
            self.board.place_piece(Lance(-1), (0, 8))

        # Knights
        self.board.place_piece(Knight(1), (8, 1))    
        self.board.place_piece(Knight(1), (8, 7))
        self.board.place_piece(Knight(-1), (0, 1))  
        self.board.place_piece(Knight(-1), (0, 7)) 

        # Silver Generals
        self.board.place_piece(Silver(1), (8, 2))
        self.board.place_piece(Silver(1), (8, 6))
        self.board.place_piece(Silver(-1), (0, 2))
        self.board.place_piece(Silver(-1), (0, 6))

        # Gold Generals
        self.board.place_piece(Gold(1), (8, 3))
        self.board.place_piece(Gold(1), (8, 5))
        self.board.place_piece(Gold(-1), (0, 3))
        self.board.place_piece(Gold(-1), (0, 5))

        # Kings
        self.board.place_piece(King(1), (8, 4))
        self.board.place_piece(King(-1), (0, 4))

        # Bishops and Rooks
        self.board.place_piece(Bishop(1), (7, 1))
        self.board.place_piece(Bishop(-1), (1, 7))
        self.board.place_piece(Rook(1), (7, 7))
        self.board.place_piece(Rook(-1),(1, 1))

    def move_piece(self, start, end):
        if self.board.move_piece(start, end):  
            piece = self.board.grid[end[0]] [end[1]] 
            if self.is_promotion_zone(end, piece):
                piece.promote()
            self.current_player *= -1  # Switch player
            return True
        return False

    def drop_piece(self, piece, position):
        if self.board.drop_piece(piece, position):
            self.current_player *= -1  # Switch player    
            return True
        return False

    def is_promotion_zone(self, position, piece):
        row, _ = position
        return (piece.player == 1 and row <= 2) or (piece.player == -1 and row >= 6)  
