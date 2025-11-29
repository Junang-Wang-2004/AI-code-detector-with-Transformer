class TicTacToe:
    def __init__(self, n):
        self.board_size = n
        self.rows_p1 = [0] * n
        self.rows_p2 = [0] * n
        self.cols_p1 = [0] * n
        self.cols_p2 = [0] * n
        self.main_diag_p1 = 0
        self.main_diag_p2 = 0
        self.anti_diag_p1 = 0
        self.anti_diag_p2 = 0

    def move(self, r, c, p):
        if p == 1:
            self.rows_p1[r] += 1
            self.cols_p1[c] += 1
            if r == c:
                self.main_diag_p1 += 1
            if r + c == self.board_size - 1:
                self.anti_diag_p1 += 1
            if (self.rows_p1[r] == self.board_size or
                self.cols_p1[c] == self.board_size or
                self.main_diag_p1 == self.board_size or
                self.anti_diag_p1 == self.board_size):
                return 1
        else:
            self.rows_p2[r] += 1
            self.cols_p2[c] += 1
            if r == c:
                self.main_diag_p2 += 1
            if r + c == self.board_size - 1:
                self.anti_diag_p2 += 1
            if (self.rows_p2[r] == self.board_size or
                self.cols_p2[c] == self.board_size or
                self.main_diag_p2 == self.board_size or
                self.anti_diag_p2 == self.board_size):
                return 2
        return 0
