class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        achievable = set(baseCosts)
        for topping in toppingCosts:
            updated = set()
            for current in achievable:
                updated.add(current)
                updated.add(current + topping)
                updated.add(current + 2 * topping)
            achievable = updated
        return min(achievable, key=lambda val: (abs(val - target), val))
