import functools

class C1:

    def findRotateSteps(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = {}
        for v4, v5 in enumerate(a1):
            v3.setdefault(v5, []).append(v4)

        @functools.lru_cache(None)
        def search(a1, a2):
            if a1 == v2:
                return 0
            v1 = float('inf')
            for v2 in v3[a2[a1]]:
                v3 = abs(a2 - v2)
                v1 = min(v1, min(v3, v1 - v3) + search(a1 + 1, v2))
            return v1
        return search(0, 0) + v2
