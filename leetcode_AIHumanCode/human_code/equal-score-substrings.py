# Time:  O(n)
# Space: O(1)

# prefix sum
class Solution(object):
    def scoreBalance(self, s):
        """
        """
        total = sum(ord(x)-ord('a')+1 for x in s)
        prefix = 0
        for x in s:
            prefix += ord(x)-ord('a')+1
            if prefix == total-prefix:
                return True
        return False
