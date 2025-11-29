# Time:  O(x)
# Space: O(x)

# memoization
class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        """
        def memoization(x):
            if y >= x:
                return y-x
            if x not in lookup:
                lookup[x] = min(x-y, min(min(x%d, d-x%d)+memoization(x//d+int(d-x%d < x%d))+1 for d in (5, 11)))
            return lookup[x]
    
        lookup = {}
        return memoization(x)


