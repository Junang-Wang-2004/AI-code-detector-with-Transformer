from functools import reduce
# Time:  O(1)
# Space: O(1)
# math
class Solution2(object):
    def numberOfWays(self, n):
        """
        """
        MOD = 10**9+7
        def count_1_2_6(n):
            # sum((n-6*i)//2+1 for i in xrange((n//6)+1))
            # = sum(((n//2)+1)-3*i for i in xrange((n//6)+1))
            return (n//2+1)*((n//6)-0+1)-3*((n//6)+0)*((n//6)-0+1)//2

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in range(min(n//4, 2)+1)), 0)


