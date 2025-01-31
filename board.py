# Board and captured piece management
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(9)]
        self.captured_pieces = {1: [], -1: []} # Player 1 and Player 2's captured pieces

    def place_piece(self, piece, position):
        self.grid[position[0]] [position[1]] = piece

    def move_piece(self, start, end):
        piece = self.grid[start[0]] [start[1]]    
        if piece and piece.can_move(start, end, self.grid):
            captured = self.grid[end[0]] [end[1]] 
            if captured:

                self.captured_pieces[piece.player].append(captured) # Capture opponent's piece
            self.grid[end[0]] [end[1]] = piece
            self.grid[start[0]] [start[1]] = None
            return True
        return False
    
    def drop_piece(self, piece, position):
        """Drop  a captured piece onto the board."""
        if self.grid[position[0]] [position[1]] is None:
            self.grid[position[0]] [position[1]] = piece
            self.captured_pieces[piece.player].remove(piece)
            return True
        return False
    
    def display(self):
        for row in self.grid:
            print(' '.join([p.name if p else '.' for p in row]))
