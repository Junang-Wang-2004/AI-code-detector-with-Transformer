class C1:

    def __init__(self, a1):
        self.board_size = a1
        self.rows_p1 = [0] * a1
        self.rows_p2 = [0] * a1
        self.cols_p1 = [0] * a1
        self.cols_p2 = [0] * a1
        self.main_diag_p1 = 0
        self.main_diag_p2 = 0
        self.anti_diag_p1 = 0
        self.anti_diag_p2 = 0

    def move(self, a1, a2, a3):
        if a3 == 1:
            self.rows_p1[a1] += 1
            self.cols_p1[a2] += 1
            if a1 == a2:
                self.main_diag_p1 += 1
            if a1 + a2 == self.board_size - 1:
                self.anti_diag_p1 += 1
            if self.rows_p1[a1] == self.board_size or self.cols_p1[a2] == self.board_size or self.main_diag_p1 == self.board_size or (self.anti_diag_p1 == self.board_size):
                return 1
        else:
            self.rows_p2[a1] += 1
            self.cols_p2[a2] += 1
            if a1 == a2:
                self.main_diag_p2 += 1
            if a1 + a2 == self.board_size - 1:
                self.anti_diag_p2 += 1
            if self.rows_p2[a1] == self.board_size or self.cols_p2[a2] == self.board_size or self.main_diag_p2 == self.board_size or (self.anti_diag_p2 == self.board_size):
                return 2
        return 0
