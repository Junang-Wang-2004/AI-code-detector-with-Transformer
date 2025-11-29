class Solution(object):
    def maxBalancedShipments(self, weight):
        ans = 0
        current = 0
        idx = 0
        n = len(weight)
        while idx < n:
            val = weight[idx]
            if val < current:
                ans += 1
                current = 0
            else:
                current = val
            idx += 1
        return ans
