class Solution:
    def numRookCaptures(self, board):
        rook_row = rook_col = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row, rook_col = i, j
                    break
            else:
                continue
            break
        
        count = 0
        
        for j in range(rook_col + 1, 8):
            ch = board[rook_row][j]
            if ch == 'p':
                count += 1
                break
            if ch != '.':
                break
        
        for j in range(rook_col - 1, -1, -1):
            ch = board[rook_row][j]
            if ch == 'p':
                count += 1
                break
            if ch != '.':
                break
        
        for i in range(rook_row + 1, 8):
            ch = board[i][rook_col]
            if ch == 'p':
                count += 1
                break
            if ch != '.':
                break
        
        for i in range(rook_row - 1, -1, -1):
            ch = board[i][rook_col]
            if ch == 'p':
                count += 1
                break
            if ch != '.':
                break
        
        return count
