from functools import reduce
# Time:  O(logb)
# Space: O(logb)
# hash table, bitmasks, combinatorics
class Solution2(object):
    def numberCount(self, a, b):
        """
        """
        fact = [1]*2
        def nPr(n, k):
            while len(fact) <= n:  # lazy initialization
                fact.append(fact[-1]*len(fact))
            return fact[n]//fact[n-k]
        
        def popcount(x):
            return bin(x).count('1')

        def count(x):
            digits = list(map(int, str(x)))
            result = 9*sum(nPr(9, i) for i in range(len(digits)-1))
            lookup = 0
            for i, d in enumerate(digits):
                mask = lookup&(((1<<d)-1)-int(i == 0))
                result += ((d-int(i == 0))-popcount(mask))*nPr(10-(i+1), len(digits)-(i+1))
                if lookup&(1<<d):
                    break
                lookup |= 1<<d
            return result

        return count(b+1)-count(a)


