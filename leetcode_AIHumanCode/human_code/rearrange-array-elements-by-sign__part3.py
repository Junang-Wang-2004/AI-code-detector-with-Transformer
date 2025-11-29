# Time:  O(n)
# Space: O(n)
# array, implementation
class Solution3(object):
    def rearrangeArray(self, nums):
        """
        """
        pos, neg = [], []
        for i in reversed(range(len(nums))):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        result = []
        for i in range(len(nums)):
            if i%2 == 0:
                result.append(pos.pop())
            else:
                result.append(neg.pop())
        return result
