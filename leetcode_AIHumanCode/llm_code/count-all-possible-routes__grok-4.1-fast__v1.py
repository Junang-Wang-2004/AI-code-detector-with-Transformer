class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9 + 7
        n = len(locations)
        ways = [[0] * (fuel + 1) for _ in range(n)]
        ways[start][0] = 1
        for spent in range(fuel + 1):
            for curr in range(n):
                for nxt in range(n):
                    if curr == nxt:
                        continue
                    d = abs(locations[curr] - locations[nxt])
                    new_spent = spent + d
                    if new_spent <= fuel:
                        ways[nxt][new_spent] = (ways[nxt][new_spent] + ways[curr][spent]) % MOD
        ans = 0
        for i in range(fuel + 1):
            ans = (ans + ways[finish][i]) % MOD
        return ans
