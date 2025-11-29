class Solution:
    def combinationSum4(self, nums, target):
        cache = {}
        def ways_to_make(amt):
            if amt == 0:
                return 1
            if amt in cache:
                return cache[amt]
            result = 0
            for val in nums:
                if val <= amt:
                    result += ways_to_make(amt - val)
            cache[amt] = result
            return result
        return ways_to_make(target)
