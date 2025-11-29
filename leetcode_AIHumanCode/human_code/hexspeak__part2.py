# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def toHexspeak(self, num):
        """
        """
        result = hex(int(num)).upper()[2:].replace('0', 'O').replace('1', 'I')
        return result if all(c in "ABCDEFOI" for c in result) else "ERROR"
