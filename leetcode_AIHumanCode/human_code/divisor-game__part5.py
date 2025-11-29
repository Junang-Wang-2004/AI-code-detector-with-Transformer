# Time:  O(n^2)
# Space: O(n)
# memoization
class Solution5(object):
    def divisorGame(self, n):
        """
        """
        def factors(n):
            for i in range(1, n+1):
                if n%i:
                    continue
                yield i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)
