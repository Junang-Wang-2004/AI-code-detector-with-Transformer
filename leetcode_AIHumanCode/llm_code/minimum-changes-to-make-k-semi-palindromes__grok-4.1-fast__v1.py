class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = n + 1
        divs = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            j = i
            while j <= n:
                divs[j].append(i)
                j += i
        min_cost = [[INF] * n for _ in range(n)]
        for leng in range(1, n + 1):
            for st in range(n - leng + 1):
                en = st + leng - 1
                for dd in divs[leng]:
                    if dd == leng:
                        continue
                    nb = leng // dd
                    cur_cost = 0
                    for pp in range(nb // 2):
                        bs1 = st + pp * dd
                        bs2 = st + (nb - 1 - pp) * dd
                        for qq in range(dd):
                            if s[bs1 + qq] != s[bs2 + qq]:
                                cur_cost += 1
                    min_cost[st][en] = min(min_cost[st][en], cur_cost)
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for nump in range(1, k + 1):
            for pos in range(1, n + 1):
                for prev in range(pos):
                    cc = min_cost[prev][pos - 1]
                    if cc < INF and dp[prev][nump - 1] < INF:
                        dp[pos][nump] = min(dp[pos][nump], dp[prev][nump - 1] + cc)
        ans = dp[n][k]
        return ans if ans < INF else n
