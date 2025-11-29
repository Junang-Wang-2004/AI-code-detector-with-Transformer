class Solution(object):
    def maxGcdSum(self, nums, k):
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        max_val = 0
        gcd_to_minstart = {}
        for end in range(n):
            updates = {}
            for old_g, beg in gcd_to_minstart.items():
                ng = gcd(old_g, nums[end])
                if ng not in updates or beg < updates[ng]:
                    updates[ng] = beg
            # new segment
            ng = nums[end]
            beg = end
            if ng not in updates or beg < updates[ng]:
                updates[ng] = beg
            gcd_to_minstart = updates
            # check valid segments
            thresh = end - k + 1
            for g, beg in gcd_to_minstart.items():
                if beg <= thresh:
                    segsum = prefix[end + 1] - prefix[beg]
                    max_val = max(max_val, g * segsum)
        return max_val
