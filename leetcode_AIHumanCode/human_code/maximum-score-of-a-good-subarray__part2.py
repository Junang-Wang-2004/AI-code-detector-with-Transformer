# Time:  O(nlogn)
# Space: O(n)
import bisect


class Solution2(object):
    def maximumScore(self, nums, k):
        """
        """
        def score(nums, k):
            prefix = [nums[k]]*(k+1)
            for i in reversed(range(k)):
                prefix[i] = min(prefix[i+1], nums[i])
            result = right = nums[k]
            for j in range(k+1, len(nums)):
                right = min(right, nums[j])
                i = bisect.bisect_left(prefix, right)
                if i >= 0:
                    result = max(result, right*(j-i+1))
            return result

        return max(score(nums, k), score(nums[::-1], len(nums)-1-k))
 
