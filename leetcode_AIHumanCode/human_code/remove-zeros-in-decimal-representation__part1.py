# Time:  O(logn)
# Space: O(1)

# math
class Solution(object):
    def removeZeros(self, n):
        """
        """
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result
    
        result = 0
        while n:
            n, r = divmod(n, 10)
            if r:
                result = result*10+r
        return reverse(result)


