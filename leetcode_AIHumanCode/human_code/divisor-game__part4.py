# Time:  O(n^(3/2))
# Space: O(n)
# memoization
class Solution4(object):
    def divisorGame(self, n):
        """
        """
        def factors(n):
            for i in range(1, n+1):
                if i*i > n:
                    break
                if n%i:
                    continue
                yield i
                if n//i != i:
                    yield n//i
    
        def memoization(n):
            if lookup[n] is None:
                lookup[n] = any(not memoization(n-i) for i in factors(n) if i != n)
            return lookup[n]

        lookup = [None]*(n+1)
        return memoization(n)


