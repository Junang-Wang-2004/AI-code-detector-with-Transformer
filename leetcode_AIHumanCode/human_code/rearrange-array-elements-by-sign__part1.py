# Time:  O(n)
# Space: O(1)

# two pointers
class Solution(object):
    def rearrangeArray(self, nums):
        """
        """
        pos, neg = 0, 1
        result = [0]*len(nums)
        for x in nums:
            if x > 0:
                result[pos] = x
                pos += 2
            else:
                result[neg] = x
                neg += 2
        return result


