class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        n = len(board)
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in deltas:
            nr, nc = rMove + dr, cMove + dc
            cnt = 0
            while 0 <= nr < n and 0 <= nc < n and board[nr][nc] != '.' and board[nr][nc] != color:
                cnt += 1
                nr += dr
                nc += dc
            if cnt > 0 and 0 <= nr < n and 0 <= nc < n and board[nr][nc] == color:
                return True
        return False
