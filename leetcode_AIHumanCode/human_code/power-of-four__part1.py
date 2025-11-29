# Time:  O(1)
# Space: O(1)

class Solution(object):
    def isPowerOfFour(self, num):
        """
        """
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)


