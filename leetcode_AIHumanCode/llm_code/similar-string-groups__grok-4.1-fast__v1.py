class Solution:
    def numSimilarGroups(self, strs):
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        par = list(range(n))
        rnk = [0] * n

        def get(x):
            if par[x] != x:
                par[x] = get(par[x])
            return par[x]

        def merge(x, y):
            px = get(x)
            py = get(y)
            if px == py:
                return
            if rnk[px] < rnk[py]:
                par[px] = py
            elif rnk[px] > rnk[py]:
                par[py] = px
            else:
                par[py] = px
                rnk[px] += 1

        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        diff += 1
                        if diff > 2:
                            break
                if diff == 2:
                    merge(i, j)

        comp = set(get(i) for i in range(n))
        return len(comp)
