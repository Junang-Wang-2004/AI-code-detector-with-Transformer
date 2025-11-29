# Time:  O(n)
# Space: O(min(n, k))
import collections


# prefix sum, freq table
class Solution2(object):
    def numGoodSubarrays(self, nums, k):
        """
        """
        result = prefix = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        for x in nums:
            prefix = (prefix+x)%k
            result += cnt[prefix]
            cnt[prefix] += 1
        l = 0
        for i in range(len(nums)):
            l += 1
            if i+1 == len(nums) or nums[i+1] != nums[i]:
                for j in range(1, l+1):
                    if nums[i]*j%k == 0:
                        result -= (l-j+1)-1
                l = 0
        return result
