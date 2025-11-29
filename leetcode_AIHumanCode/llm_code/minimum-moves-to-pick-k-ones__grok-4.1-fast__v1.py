class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        pos = []
        for i in range(len(nums)):
            if nums[i]:
                pos.append(i)
        t = len(pos)
        pref = [0] * (t + 1)
        for j in range(t):
            pref[j + 1] = pref[j] + pos[j]
        res = float('inf')
        for added in range(min(k, maxChanges) + 1):
            needed = k - added
            if needed > t or needed <= 0:
                continue
            extra_cost = added * 2
            width = needed
            md = width // 2
            for begin in range(t - width + 1):
                left_total = pref[begin + md] - pref[begin]
                right_total = pref[begin + width] - pref[begin + width - md]
                move_cost = right_total - left_total
                res = min(res, extra_cost + move_cost)
        return res
