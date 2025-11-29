class Solution:
    def combinationSum3(self, k, n):
        ans = []
        def backtrack(path, total, pos):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return
            for num in range(pos, 10):
                if total + num > n:
                    break
                path.append(num)
                backtrack(path, total + num, num + 1)
                path.pop()
        backtrack([], 0, 1)
        return ans
