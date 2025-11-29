from functools import reduce
# Time:  O(n)
# Space: O(1)
# math
class Solution3(object):
    def numberOfWays(self, n):
        """
        """
        MOD = 10**9+7
        def count_1_2(n):
            return n//2+1
    
        def count_1_2_6(n):
            return sum(count_1_2(n-6*i) for i in range((n//6)+1))

        return reduce(lambda x, y: (x+count_1_2_6(n-4*y))%MOD, (i for i in range(min(n//4, 2)+1)), 0)


