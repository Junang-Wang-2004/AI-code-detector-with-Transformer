class Solution(object):
    def maxCaloriesBurnt(self, heights):
        h = sorted(heights)
        i = 0
        j = len(h) - 1
        res = h[j] * h[j]
        while i < j:
            res += (h[j] - h[i]) * (h[j] - h[i])
            j -= 1
            if i < j:
                res += (h[i] - h[j]) * (h[i] - h[j])
                i += 1
        return res
