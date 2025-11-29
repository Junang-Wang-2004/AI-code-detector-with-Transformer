# Time:  O(logn)
# Space: O(1)

# string, bitmasks
class Solution(object):
    def isFascinating(self, n):
        """
        """
        lookup = [0]
        def check(x):
            while x:
                x, d = divmod(x, 10)
                if d == 0 or lookup[0]&(1<<d):
                    return False
                lookup[0] |= (1<<d)
            return True
    
        return check(n) and check(2*n) and check(3*n)


