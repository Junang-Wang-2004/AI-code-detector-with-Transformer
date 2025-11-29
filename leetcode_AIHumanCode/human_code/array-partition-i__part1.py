# Time:  O(r), r is the range size of the integers
# Space: O(r)


class Solution(object):
    def arrayPairSum(self, nums):
        """
        """
        LEFT, RIGHT = -10000, 10000
        lookup = [0] * (RIGHT-LEFT+1)
        for num in nums:
            lookup[num-LEFT] += 1
        r, result = 0, 0
        for i in range(LEFT, RIGHT+1):
            result += (lookup[i-LEFT] + 1 - r) / 2 * i
            r = (lookup[i-LEFT] + r) % 2
        return result


