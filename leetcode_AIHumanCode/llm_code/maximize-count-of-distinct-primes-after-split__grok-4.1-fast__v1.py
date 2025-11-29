from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def maximumCount(self, nums, queries):
        MAX = 100010
        spf = list(range(MAX))
        for i in range(2, int(MAX ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def isprime(val):
            return 1 <= val < MAX and spf[val] == val
        
        n = len(nums)
        prime_indices = defaultdict(SortedList)
        
        class RangeAddMaxQuery:
            def __init__(self, size):
                self.size = size
                self.tre = [0] * (4 * size + 10)
                self.lzy = [0] * (4 * size + 10)
            
            def _push(self, nd, lo, hi):
                if self.lzy[nd]:
                    self.tre[nd] += self.lzy[nd]
                    if lo < hi:
                        self.lzy[2 * nd] += self.lzy[nd]
                        self.lzy[2 * nd + 1] += self.lzy[nd]
                    self.lzy[nd] = 0
            
            def _modify(self, L, R, delta, nd=1, lo=0, hi=None):
                if hi is None:
                    hi = self.size - 1
                self._push(nd, lo, hi)
                if lo > R or hi < L or lo > hi:
                    return
                if L <= lo and hi <= R:
                    self.lzy[nd] += delta
                    self._push(nd, lo, hi)
                    return
                md = (lo + hi) // 2
                self._modify(L, R, delta, 2 * nd, lo, md)
                self._modify(L, R, delta, 2 * nd + 1, md + 1, hi)
                self.tre[nd] = max(self.tre[2 * nd], self.tre[2 * nd + 1])
            
            def _qry(self, L, R, nd=1, lo=0, hi=None):
                if hi is None:
                    hi = self.size - 1
                self._push(nd, lo, hi)
