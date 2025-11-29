class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        size = 1
        while size <= n:
            for k in range(size):
                if size + k <= n:
                    ans[size + k] = ans[k] + 1
            size *= 2
        return ans
