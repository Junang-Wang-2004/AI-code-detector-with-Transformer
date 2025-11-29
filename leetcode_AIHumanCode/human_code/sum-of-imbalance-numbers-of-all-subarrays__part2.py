# Time:  O(n^2)
# Space: O(n)
# hash table, two pointers
class Solution2(object):
    def sumImbalanceNumbers(self, nums):
        """
        """
        result = 0
        for right in range(len(nums)):
            lookup = {nums[right]}
            curr = 0
            for left in reversed(range(right)):
                if nums[left] not in lookup:
                    lookup.add(nums[left])
                    curr += 1-(nums[left]-1 in lookup)-(nums[left]+1 in lookup)
                result += curr
        return result
