class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        group_max = {}
        for key, value in zip(x, y):
            if key not in group_max or value > group_max[key]:
                group_max[key] = value
        maxima = list(group_max.values())
        if len(maxima) < 3:
            return -1
        maxima.sort(reverse=True)
        return sum(maxima[:3])
