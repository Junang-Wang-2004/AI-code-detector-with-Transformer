from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        BOARD_SIZE = 50
        INF = float('inf')
        NINF = float('-inf')
        knight_moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        def compute_knight_dists(srow, scol):
            board_dist = [[INF] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            board_dist[srow][scol] = 0
            queue = deque([(srow, scol)])
            while queue:
                row, col = queue.popleft()
                curr_dist = board_dist[row][col]
                for drow, dcol in knight_moves:
                    nrow, ncol = row + drow,
