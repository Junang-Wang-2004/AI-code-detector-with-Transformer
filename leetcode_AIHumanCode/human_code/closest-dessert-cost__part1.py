# Time:  O(m * max(max_base, target + max_topping / 2)) ~= O(m * t)
# Space: O(max(max_base, target + max_topping / 2)) ~= O(t)

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        """
        max_count = 2
        max_base, max_topping = max(baseCosts), max(toppingCosts)
        dp = [False]*(max(max_base, target+max_topping//2)+1)
        for b in baseCosts:
            dp[b] = True
        for t in toppingCosts:
            for _ in range(max_count):
                for i in reversed(range(len(dp)-t)):
                    if dp[i]:
                        dp[i+t] = True
        result = float("inf")
        for i in range(1, len(dp)):
            if not dp[i]:
                continue
            if abs(i-target) < abs(result-target):
                result = i
            if i >= target:
                break
        return result
            

