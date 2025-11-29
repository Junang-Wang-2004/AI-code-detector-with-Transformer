import collections
import math
from collections import defaultdict

class Solution:
    def numSquarefulPerms(self, A):
        def valid_sum(x, y):
            total = x + y
            sq = int(math.sqrt(total))
            return sq * sq == total

        freq = collections.Counter(A)
        neighbors = defaultdict(list)
        for u in list(freq):
            for v in list(freq):
                if valid_sum(u, v):
                    neighbors[u].append(v)

        ans = 0

        def search(prev, to_place):
            nonlocal ans
            if to_place == 0:
                ans += 1
                return
            for curr in neighbors[prev]:
                if freq[curr] > 0:
                    freq[curr] -= 1
                    search(curr, to_place - 1)
                    freq[curr] += 1

        n = len(A)
        for init in list(freq):
            if freq[init] > 0:
                freq[init] -= 1
                search(init, n - 1)
                freq[init] += 1
        return ans
