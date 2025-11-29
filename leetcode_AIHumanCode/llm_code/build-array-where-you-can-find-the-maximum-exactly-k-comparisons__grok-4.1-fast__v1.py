class Solution(object):
    def numOfArrays(self, n, m, k):
        MOD = 10**9 + 7
        prev = [[0] * (k + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            prev[i][1] = 1
        for length in range(2, n + 1):
            pref = [[0] * (m + 1) for _ in range(k + 1)]
            for j in range(k + 1):
                for i in range(1, m + 1):
                    pref[j][i] = (pref[j][i - 1] + prev[i][j]) % MOD
            curr = [[0] * (k + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, k + 1):
                    retain = prev[i][j] * i % MOD
                    update = pref[j - 1][i - 1]
                    curr[i][j] = (retain + update) % MOD
            prev = curr
        return sum(prev[i][k] for i in range(1, m + 1)) % MOD
