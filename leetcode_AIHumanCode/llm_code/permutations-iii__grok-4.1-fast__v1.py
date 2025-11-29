class Solution:
    def permute(self, n):
        ans = []
        visited = [False] * (n + 1)
        
        def dfs(path):
            if len(path) == n:
                ans.append(list(path))
                return
            for num in range(1, n + 1):
                if (not visited[num] and
                    (not path or path[-1] % 2 != num % 2)):
                    visited[num] = True
                    path.append(num)
                    dfs(path)
                    path.pop()
                    visited[num] = False
        
        dfs([])
        return ans
