class Solution:
    def numIslands(self, board):
        if not board or not board[0]:
            return 0
        rows, cols = len(board), len(board[0])
        def flood(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != '1':
                return
            board[r][c] = '0'
            flood(r + 1, c)
            flood(r - 1, c)
            flood(r, c + 1)
            flood(r, c - 1)
        result = 0
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == '1':
                    result += 1
                    flood(x, y)
        return result
