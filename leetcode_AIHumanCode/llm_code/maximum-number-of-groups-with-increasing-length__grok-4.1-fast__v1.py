class Solution:
    def maxIncreasingGroups(self, usageLimits):
        n = len(usageLimits)
        capacities = sorted(min(limit, n) for limit in usageLimits)
        num_groups = 0
        surplus = 0
        for capacity in capacities:
            surplus += capacity
            while surplus >= num_groups + 1:
                surplus -= num_groups + 1
                num_groups += 1
        return num_groups
