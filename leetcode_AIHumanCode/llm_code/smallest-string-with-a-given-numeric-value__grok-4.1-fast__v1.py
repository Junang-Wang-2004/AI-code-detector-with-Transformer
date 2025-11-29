class Solution(object):
    def getSmallestString(self, n, k):
        """
        """
        output = []
        for pos in range(n):
            spots_left = n - pos - 1
            char_val = max(1, k - 26 * spots_left)
            output.append(chr(ord('a') + char_val - 1))
            k -= char_val
        return "".join(output)
