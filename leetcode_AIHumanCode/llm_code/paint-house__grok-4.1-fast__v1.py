class Solution:
    def minCost(self, costs):
        if not costs:
            return 0
        prev0, prev1, prev2 = costs[0]
        for house in costs[1:]:
            curr0 = house[0] + min(prev1, prev2)
            curr1 = house[1] + min(prev0, prev2)
            curr2 = house[2] + min(prev0, prev1)
            prev0, prev1, prev2 = curr0, curr1, curr2
        return min(prev0, prev1, prev2)
