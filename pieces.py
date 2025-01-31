class Piece:
    def __init__(self, name, player):
        self.name = name  # Piece name (e.g., P, L, K)
        self.player = player  # 1 for Player 1, -1 for Player 2
        self.promoted = False

    def promote(self):
        self.promoted = True

    def can_move(self, start, end, board):
        raise NotImplementedError


class Pawn(Piece):
    def __init__(self, player):
        super().__init__('歩', player)  # Use Kanji for authenticity

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        return row_diff == self.player and col_diff == 0


class Lance(Piece):
    def __init__(self, player):
        super().__init__('香', player)

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        if col_diff != 0:
            return False
        step = 1 if row_diff > 0 else -1
        for r in range(start[0] + step, end[0], step):
            if board[r][start[1]] is not None:
                return False
        return row_diff * self.player > 0


class Knight(Piece):
    def __init__(self, player):
        super().__init__('桂', player)

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])
        return row_diff == 2 * self.player and col_diff == 1


class Silver(Piece):
    def __init__(self, player):
        super().__init__('銀', player)

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])
        return (row_diff == self.player and col_diff <= 1) or (abs(row_diff) == 1 and col_diff == 1)


class Gold(Piece):
    def __init__(self, player):
        super().__init__('金', player)

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])
        return (row_diff == self.player and col_diff <= 1) or (row_diff == 0 and col_diff == 1)


class King(Piece):
    def __init__(self, player):
        super().__init__('玉' if player == 1 else '王', player)

    def can_move(self, start, end, board):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        return row_diff <= 1 and col_diff <= 1


class Bishop(Piece):
    def __init__(self, player):
        super().__init__('角', player)

    def can_move(self, start, end, board):
        row_diff = abs(end[0] - start[0])
        col_diff = abs(end[1] - start[1])
        if row_diff != col_diff:
            return False
        step_row = 1 if end[0] > start[0] else -1
        step_col = 1 if end[1] > start[1] else -1
        for i in range(1, row_diff):
            if board[start[0] + i * step_row][start[1] + i * step_col] is not None:
                return False
        return True


class Rook(Piece):
    def __init__(self, player):
        super().__init__('飛', player)

    def can_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        if row_diff != 0 and col_diff != 0:
            return False
        if row_diff == 0:
            step = 1 if col_diff > 0 else -1
            for c in range(start[1] + step, end[1], step):
                if board[start[0]][c] is not None:
                    return False
        else:
            step = 1 if row_diff > 0 else -1
            for r in range(start[0] + step, end[0], step):
                if board[r][start[1]] is not None:
                    return False
        return True