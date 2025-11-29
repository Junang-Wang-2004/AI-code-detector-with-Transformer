# Time:  O(dlogd), d is the number of digits
# Space: O(d)
# greedy
class Solution2(object):
    def smallestNumber(self, num):
        """
        """
        sign = 1 if num >= 0 else -1
        nums = sorted(str(abs(num)), reverse=(sign == -1))
        i = next((i for i in range(len(nums)) if nums[i] != '0'), 0)
        nums[0], nums[i] = nums[i], nums[0]
        return sign*int("".join(nums))
