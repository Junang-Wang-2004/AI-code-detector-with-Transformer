class Solution:
    def minCost(self, nums, cost):
        pairs = sorted(zip(nums, cost))
        total_weight = sum(w for _, w in pairs)
        cum_weight = 0
        threshold = (total_weight + 1) // 2
        target_val = 0
        for val, w in pairs:
            cum_weight += w
            if cum_weight >= threshold:
                target_val = val
                break
        return sum(abs(val - target_val) * w for val, w in pairs)
