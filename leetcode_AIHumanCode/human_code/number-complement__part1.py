# Time:  O(1)
# Space: O(1)

class Solution(object):
    def findComplement(self, num):
        """
        """
        return 2 ** (len(bin(num)) - 2) - 1 - num


