class C1(object):

    def __init__(self, a1):
        self.board = [row for v1 in a1 if v1]
        self.cur_r = 0
        self.cur_c = 0

    def __next__(self):
        v1 = self.board[self.cur_r][self.cur_c]
        self.cur_c += 1
        if self.cur_c == len(self.board[self.cur_r]):
            self.cur_r += 1
            self.cur_c = 0
        return v1

    def hasNext(self):
        if self.cur_r >= len(self.board):
            return False
        return self.cur_c < len(self.board[self.cur_r])
