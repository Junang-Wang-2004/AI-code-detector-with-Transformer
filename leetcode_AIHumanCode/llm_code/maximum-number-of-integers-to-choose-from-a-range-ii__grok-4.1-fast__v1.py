class Solution:
    def maxCount(self, banned, n, maxSum):
        forbidden = set(banned)
        cnt = 0
        sm = 0
        val = 1
        while val <= n:
            if val in forbidden:
                val += 1
                continue
            if sm + val > maxSum:
                break
            sm += val
            cnt += 1
            val += 1
        return cnt
