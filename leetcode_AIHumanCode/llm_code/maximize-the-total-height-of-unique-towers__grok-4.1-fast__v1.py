class Solution:
    def maximumTotalSum(self, maximumHeight):
        heights = sorted(maximumHeight, reverse=True)
        total = 0
        cap = float('inf')
        for mh in heights:
            h = min(mh, cap - 1)
            if h < 1:
                return -1
            total += h
            cap = h
        return total
