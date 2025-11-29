# Time:  O(nlogr), r = max(max(a), max(b), max(c))
# Space: O(1)
# bit manipulation, parity
class Solution2(object):
    def tripletCount(self, a, b, c):
        """
        """
        def popcount(x):
            return bin(x).count('1')

        def count(a):
            odd = sum(popcount(x)&1 for x in a)
            return [len(a)-odd, odd]
        
        even1, odd1 = count(a)
        even2, odd2 = count(b)
        even3, odd3 = count(c)
        return even1*even2*even3 + even1*odd2*odd3 + odd1*even2*odd3 + odd1*odd2*even3


