class Vector2D(object):

    def __init__(self, vec2d):
        self.board = [row for row in vec2d if row]
        self.cur_r = 0
        self.cur_c = 0

    def __next__(self):
        val = self.board[self.cur_r][self.cur_c]
        self.cur_c += 1
        if self.cur_c == len(self.board[self.cur_r]):
            self.cur_r += 1
            self.cur_c = 0
        return val

    def hasNext(self):
        if self.cur_r >= len(self.board):
            return False
        return self.cur_c < len(self.board[self.cur_r])
