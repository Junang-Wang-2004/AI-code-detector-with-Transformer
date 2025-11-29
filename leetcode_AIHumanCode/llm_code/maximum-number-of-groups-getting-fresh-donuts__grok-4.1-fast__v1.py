from functools import lru_cache
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        freq = [0] * batchSize
        for g in groups:
            freq[g % batchSize] += 1
        total = freq[0]
        freq[0] = 0
        for k in range(1, batchSize // 2 + 1):
            m = batchSize - k
            num_pairs = freq[k] // 2 if k == m else min(freq[k], freq[m])
            total += num_pairs
            freq[k] -= num_pairs
            if k != m:
                freq[m] -= num_pairs
        active = [r for r in range(1, batchSize) if freq[r]]
        if not active:
            return total
        init_state = tuple(freq[r] for r in active)
        @lru_cache(maxsize=None)
        def rec(pending: int, counts: tuple) -> int:
            if not any(counts):
                return 0
            best = 0
            for idx, sz in enumerate(active):
                if counts[idx]:
                    next_pending = (pending - sz) % batchSize
                    next_counts = list(counts)
                    next_counts[idx] -= 1
                    bonus = 1 if next_pending == 0 else 0
                    best = max(best, bonus + rec(next_pending, tuple(next_counts)))
            return best
        return total + rec(0, init_state)
