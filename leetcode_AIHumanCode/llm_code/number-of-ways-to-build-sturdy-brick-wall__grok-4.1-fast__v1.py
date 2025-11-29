class Solution:
    def buildWall(self, height, width, bricks):
        MOD = 10**9 + 7
        reachable = [set() for _ in range(width + 1)]
        reachable[0].add(0)
        for pos in range(width):
            for mask in reachable[pos]:
                for sz in bricks:
                    new_pos = pos + sz
                    if new_pos > width:
                        continue
                    new_mask = mask | (1 << new_pos)
                    reachable[new_pos].add(new_mask)
        patterns = [m ^ (1 << width) for m in reachable[width]]
        n = len(patterns)
        adj = [[k for k in range(n) if (patterns[k] & patterns[j]) == 0] for j in range(n)]
        prev_ways = [1] * n
        for _ in range(height - 1):
            curr_ways = [0] * n
            for j in range(n):
                s = 0
                for k in adj[j]:
                    s = (s + prev_ways[k]) % MOD
                curr_ways[j] = s
            prev_ways = curr_ways
        return sum(prev_ways) % MOD
