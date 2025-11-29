from collections import defaultdict

class Solution(object):
    cache = {}

    def chain_length(self, start):
        if start in self.cache:
            return self.cache[start]
        steps = 0
        current = start
        while current > 1:
            if current in self.cache:
                steps += self.cache[current]
                break
            steps += 1
            current = current // 2 if current % 2 == 0 else 3 * current + 1
        self.cache[start] = steps
        return steps

    def getKth(self, lo, hi, k):
        buckets = defaultdict(list)
        for val in range(lo, hi + 1):
            length = self.chain_length(val)
            buckets[length].append(val)
        ordered_lengths = sorted(buckets)
        accumulated = 0
        for length in ordered_lengths:
            group = buckets[length]
            group_size = len(group)
            if accumulated + group_size >= k:
                return group[k - accumulated - 1]
            accumulated += group_size
