class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        MOD = 10**9 + 7
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for x in range(n - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if num[x] == num[y]:
                    lcp[x][y] = lcp[x + 1][y + 1] + 1
        def seg_leq(a: int, b: int, ln: int) -> bool:
            pref = lcp[a][b]
            if pref >= ln:
                return True
            return num[a + pref] < num[b + pref]
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        psum = [[0] * (n + 2) for _ in range(n + 1)]
        for leng in range(1, n + 1):
            for sz in range(1, leng + 1):
                begin = leng - sz
                if num[begin] == '0':
                    dp[leng][sz] = 0
                else:
                    if begin == 0:
                        dp[leng][sz] = 1
                    else:
                        tot_small = psum[begin][sz - 1]
                        tot_same = 0
                        if sz <= begin:
                            pbegin = begin - sz
                            if seg_leq(pbegin, begin, sz):
                                tot_same = dp[begin][sz]
                        dp[leng][sz] = (tot_small + tot_same) % MOD
                psum[leng][sz] = (psum[leng][sz - 1] + dp[leng][sz]) % MOD
        return psum[n][n]
