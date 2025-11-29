class Solution:
    def maxGoodNumber(self, nums):
        bitstrs = [format(x, 'b') for x in nums]
        n = len(bitstrs)
        visited = [False] * n
        max_value = 0

        def dfs(path):
            nonlocal max_value
            if len(path) == n:
                num = int(''.join(path), 2)
                if num > max_value:
                    max_value = num
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [bitstrs[i]])
                    visited[i] = False

        dfs([])
        return max_value
