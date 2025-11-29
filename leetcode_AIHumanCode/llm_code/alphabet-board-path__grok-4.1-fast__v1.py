class Solution:
    def alphabetBoardPath(self, target):
        res = []
        row, col = 0, 0
        for ch in target:
            tgt_row = (ord(ch) - 97) // 5
            tgt_col = (ord(ch) - 97) % 5
            while row > tgt_row:
                res.append('U')
                row -= 1
            while col > tgt_col:
                res.append('L')
                col -= 1
            while col < tgt_col:
                res.append('R')
                col += 1
            while row < tgt_row:
                res.append('D')
                row += 1
            res.append('!')
        return ''.join(res)
