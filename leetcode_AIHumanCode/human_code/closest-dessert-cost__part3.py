# Time:  O(3^m*log(3^m)) + O(n*log(3^m)) = O(m*(3^m + n))
# Space: O(3^m)
import bisect


class Solution3(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        """
        max_count = 2
        combs = set([0])
        for t in toppingCosts:
            combs = set([c+i*t for c in combs for i in range(max_count+1)])
        result, combs = float("inf"), sorted(combs)
        for b in baseCosts:
            idx = bisect.bisect_left(combs, target-b)
            if idx < len(combs):
                result = min(result, b+combs[idx], key=lambda x: (abs(x-target), x))
            if idx > 0:
                result = min(result, b+combs[idx-1], key=lambda x: (abs(x-target), x))        
        return result


