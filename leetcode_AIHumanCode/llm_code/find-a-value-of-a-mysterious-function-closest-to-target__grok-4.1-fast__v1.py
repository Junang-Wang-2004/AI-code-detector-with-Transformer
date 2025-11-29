class Solution:
    def closestToTarget(self, arr, target):
        ans = float("inf")
        prev_ands = set()
        for num in arr:
            curr_ands = set()
            curr_ands.add(num)
            for p in prev_ands:
                curr_ands.add(p & num)
            prev_ands = curr_ands
            for v in curr_ands:
                ans = min(ans, abs(v - target))
        return ans
