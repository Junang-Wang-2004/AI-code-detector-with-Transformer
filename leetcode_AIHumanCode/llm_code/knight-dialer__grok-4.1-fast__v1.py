class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        positions = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        graph = [[] for _ in range(10)]
        for i in range(10):
            x, y = positions[i]
            for dx, dy in knight_moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= 3 and 0 <= ny <= 2 and (nx < 3 or ny == 1):
                    next_pos = 0 if nx == 3 else nx * 3 + ny + 1
                    graph[i].append(next_pos)
        counts = [1] * 10
        for _ in range(n - 1):
            new_counts = [0] * 10
            for curr_pos in range(10):
                for next_pos in graph[curr_pos]:
                    new_counts[next_pos] = (new_counts[next_pos] + counts[curr_pos]) % MOD
            counts = new_counts
        return sum(counts) % MOD
