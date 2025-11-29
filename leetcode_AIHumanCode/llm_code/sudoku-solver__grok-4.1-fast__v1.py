class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []
        for x in range(9):
            for y in range(9):
                ch = board[x][y]
                if ch == '.':
                    empty.append((x, y))
                else:
                    mask = 1 << (int(ch) - 1)
                    rows[x] |= mask
                    cols[y] |= mask
                    boxes[(x // 3) * 3 + y // 3] |= mask
        
        def search(p):
            if p == len(empty):
                return True
            i, j = empty[p]
            b = (i // 3) * 3 + j // 3
            for d in range(9):
                m = 1 << d
                if rows[i] & m == 0 and cols[j] & m == 0 and boxes[b] & m == 0:
                    board[i][j] = str(d + 1)
                    rows[i] |= m
                    cols[j] |= m
                    boxes[b] |= m
                    if search(p + 1):
                        return True
                    board[i][j] = '.'
                    rows[i] &= ~m
                    cols[j] &= ~m
                    boxes[b] &= ~m
            return False
        
        search(0)
