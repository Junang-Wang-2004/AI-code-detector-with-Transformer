# Time:  O(n)
# Space: O(1)
from itertools import zip_longest


class Solution2(object):
    def addBinary(self, a, b):
        """
        """
        result = ""
        carry = 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry, remainder = divmod(int(x)+int(y)+carry, 2)
            result += str(remainder)
        
        if carry:
            result += str(carry)
        
        return result[::-1]
