# Time:  O(nlogn + n * k + klogn) = O(nlogn + n * k)
# Space: O(k)

# sort, dp, bitmasks
class Solution(object):
    def subsequenceSumAfterCapping(self, nums, k):
        """
        """
        result = [False]*len(nums)
        nums.sort()
        mask = (1<<(k+1))-1
        dp = 1
        i = 0
        for x in range(1, len(nums)+1):
            while i < len(nums) and nums[i] < x:
                dp |= (dp<<nums[i])&mask
                i += 1
            for j in range(max(k%x, k-(len(nums)-i)*x), k+1, x):
                if dp&(1<<j):
                    result[x-1] = True
                    break
        return result


