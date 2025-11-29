class Solution:
    def combine(self, n, k):
        ans = []
        def rec(curr, begin):
            if len(curr) == k:
                ans.append(list(curr))
                return
            for val in range(begin, n + 1):
                curr.append(val)
                rec(curr, val + 1)
                curr.pop()
        rec([], 1)
        return ans
