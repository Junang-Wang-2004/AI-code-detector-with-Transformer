# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def baseNeg2(self, N):
        """
        """
        result = []
        while N:
            result.append(str(-N & 1))  # N % -2
            N = -(N >> 1)  # N //= -2
        result.reverse()
        return "".join(result) if result else "0"


