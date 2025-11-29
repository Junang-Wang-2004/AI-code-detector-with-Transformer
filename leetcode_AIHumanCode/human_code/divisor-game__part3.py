# Time:  O(nlogn)
# Space: O(nlogn)
# memoization, number theory
class Solution3(object):
    def divisorGame(self, n):
        """
        """
        def factors(n):
            result = [[] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in FACTORS[n] if i != n)
            return lookup[n]

        FACTORS = factors(n)
        lookup = [None]*(n+1)
        return memoization(n)


