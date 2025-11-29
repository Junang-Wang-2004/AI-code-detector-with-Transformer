# Time:  O(n * 3^n)
# Space: O(3^n)
# memoization, top-down dp (easy to implement but slower)
class Solution4(object):
    def maximumANDSum(self, nums, numSlots):
        """
        """
        def memoiztion(i, mask):  # i is metadata, which could be derived from mask, just for shorter implementation
            if lookup[mask] != -1:
                return lookup[mask]
            x = nums[i] if i < len(nums) else 0
            base = 1
            for slot in range(1, numSlots+1):
                if mask//base%3:
                     lookup[mask] = max(lookup[mask], (x&slot)+memoiztion(i-1, mask-base))
                base *= 3
            return lookup[mask]
        
        lookup = [-1]*(3**numSlots)
        lookup[0] = 0
        return memoiztion(2*numSlots-1, 3**numSlots-1)
