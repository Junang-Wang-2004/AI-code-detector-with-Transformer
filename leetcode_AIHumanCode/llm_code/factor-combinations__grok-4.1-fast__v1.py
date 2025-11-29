class Solution(object):
    def getFactors(self, n):
        ans = []
        def dfs(remain, begin, trail):
            up = int(remain ** 0.5) + 1
            for j in range(begin, up):
                if remain % j == 0:
                    trail.append(j)
                    dfs(remain // j, j, trail)
                    trail.pop()
            if remain >= begin:
                trail.append(remain)
                if len(trail) >= 2:
                    ans.append(list(trail))
                trail.pop()
        dfs(n, 2, [])
        return ans
