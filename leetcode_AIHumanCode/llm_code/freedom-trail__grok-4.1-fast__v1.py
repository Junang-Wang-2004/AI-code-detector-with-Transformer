import functools

class Solution:
    def findRotateSteps(self, ring, key):
        n, m = len(ring), len(key)
        pos = {}
        for i, ch in enumerate(ring):
            pos.setdefault(ch, []).append(i)
        
        @functools.lru_cache(None)
        def search(step, here):
            if step == m:
                return 0
            best = float('inf')
            for there in pos[key[step]]:
                steps = abs(here - there)
                best = min(best, min(steps, n - steps) + search(step + 1, there))
            return best
        
        return search(0, 0) + m
