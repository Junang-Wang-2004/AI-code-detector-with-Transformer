from collections import defaultdict

class Solution:
    def maxTotal(self, value, limit):
        buckets = defaultdict(list)
        for i in range(len(value)):
            buckets[limit[i]].append(value[i])
        total = 0
        for cap, prizes in buckets.items():
            prizes.sort(reverse=True)
            total += sum(prizes[:cap])
        return total
