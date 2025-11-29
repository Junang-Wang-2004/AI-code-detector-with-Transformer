# Time:  O(n * 3^m)
# Space: O(3^m)
class Solution4(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        """
        max_count = 2
        combs = set([0])
        for t in toppingCosts:
            combs = set([c+i*t for c in combs for i in range(max_count+1)])
        result = float("inf")
        for b in baseCosts:
            for c in combs:
                result = min(result, b+c, key=lambda x: (abs(x-target), x))      
        return result
