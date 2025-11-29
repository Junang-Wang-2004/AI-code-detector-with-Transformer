# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        """
        fact = [1]*2
        def nPr(n, k):
            while len(fact) <= n:  # lazy initialization
                fact.append(fact[-1]*len(fact))
            return fact[n]//fact[n-k]

        return 1+9*sum(nPr(9, i) for i in range(n))
