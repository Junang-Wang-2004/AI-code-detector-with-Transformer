# Time:  O(n * m * logr), r = max(nums)
# Space: O(n * m * logr)
import collections


# memoization
class Solution3(object):
    def minimumValueSum(self, nums, andValues):
        """
        """
        INF = float("inf")
        FULL_MASK = (1<<max(nums).bit_length())-1
        def memoization(i, j, mask): 
            if i == len(nums) and j == len(andValues):
                return 0
            if i == len(nums) or j == len(andValues) or mask < andValues[j]:
                return INF 
            if  mask not in lookup[i][j]:
                curr = memoization(i+1, j, mask&nums[i])
                if mask&nums[i] == andValues[j]:
                    curr = min(curr, nums[i]+memoization(i+1, j+1, FULL_MASK))
                lookup[i][j][mask] = curr
            return lookup[i][j][mask]
    
        lookup = [[collections.defaultdict(int) for _ in range(len(andValues))] for _ in range(len(nums))]
        result = memoization(0, 0, FULL_MASK)
        return result if result != INF else -1
