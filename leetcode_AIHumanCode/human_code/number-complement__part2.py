# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num


