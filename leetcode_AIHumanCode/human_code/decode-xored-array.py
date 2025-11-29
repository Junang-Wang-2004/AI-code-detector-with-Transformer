# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decode(self, encoded, first):
        """
        """
        result = [first]
        for x in encoded:
            result.append(result[-1]^x)
        return result
