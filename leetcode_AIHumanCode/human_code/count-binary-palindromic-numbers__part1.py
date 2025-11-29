# Time:  O(logn)
# Space: O(1)

# bitmasks, combinatorics
class Solution(object):
    def countBinaryPalindromes(self, n):
        """
        """
        def length(n):
            result = 0
            while n:
                result += 1
                n >>= 1
            return result

        def reverse(n, l):
            result = 0
            for i in range(l):
                if n&(1<<i):
                    result |= 1<<((l-1)-i)
            return result
    
        l = length(n)//2
        return ((1<<l)-1)+(n>>l)+int(((n>>l)<<l)|reverse(n>>(length(n)-l), l) <= n)


