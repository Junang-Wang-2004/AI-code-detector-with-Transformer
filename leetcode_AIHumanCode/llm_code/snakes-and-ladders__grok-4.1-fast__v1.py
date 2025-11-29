import collections

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        N = n * n
        dist = [-1] * (N + 1)
        dist[1] = 0
        q = collections.deque([1])
        while q:
            pos = q.popleft()
            for dice in range(1, 7):
                nxt = pos + dice
                if nxt > N:
                    break
                k = (nxt - 1) // n
                r = n - 1 - k
                c = (nxt - 1) % n
                if k % 2 == 1:
                    c = n - 1 - c
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dist[dest] == -1:
                    dist[dest] = dist[pos] + 1
                    q.append(dest)
                    if dest == N:
                        return dist[N]
        return -1
