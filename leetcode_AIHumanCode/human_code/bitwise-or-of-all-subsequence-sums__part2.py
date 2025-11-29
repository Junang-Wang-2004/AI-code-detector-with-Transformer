# Time:  O(nlogn)
# Space: O(1)
# bit manipulation
class Solution2(object):
    def subsequenceSumOr(self, nums):
        """
        """
        result = cnt = 0
        for i in range(64):
            cnt >>= 1
            for x in nums:
                cnt += (x>>i)&1
            if cnt:
                result |= 1<<i
        return result
