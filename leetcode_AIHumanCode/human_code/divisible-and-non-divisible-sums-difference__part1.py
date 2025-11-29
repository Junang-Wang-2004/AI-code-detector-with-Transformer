# Time:  O(1)
# Space: O(1)

# math
class Solution(object):
    def differenceOfSums(self, n, m):
        """
        """
        def arithmetic_progression_sum(a, d, l):
            return (a+(a+(l-1)*d))*l//2
    
        return arithmetic_progression_sum(1, 1, n) - 2*arithmetic_progression_sum(m, m, n//m)


