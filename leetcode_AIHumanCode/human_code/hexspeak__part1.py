# Time:  O(n)
# Space: O(1)

class Solution(object):
    def toHexspeak(self, num):
        """
        """
        lookup = {0:'O', 1:'I'}
        for i in range(6):
            lookup[10+i] = chr(ord('A')+i)
        result = []
        n = int(num)
        while n:
            n, r = divmod(n, 16)
            if r not in lookup:
                return "ERROR"
            result.append(lookup[r])
        return "".join(reversed(result))


