# Time:  O(n * k)
# Space: O(k * 2^k)

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        """
        return 2**k <= len(s) and len({s[i:i+k] for i in range(len(s)-k+1)}) == 2**k
    

