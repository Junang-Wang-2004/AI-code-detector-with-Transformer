class C1:

    def shoppingOffers(self, a1, a2, a3):
        from functools import lru_cache
        v1 = len(a1)

        @lru_cache(None)
        def best_cost(a1):
            if all((q == 0 for v1 in a1)):
                return 0
            v2 = sum((a1[k] * a1[k] for v3 in range(v1)))
            for v4 in a2:
                if all((a1[v3] >= v4[v3] for v3 in range(v1))):
                    v5 = tuple((a1[v3] - v4[v3] for v3 in range(v1)))
                    v2 = min(v2, v4[-1] + best_cost(v5))
            return v2
        return best_cost(tuple(a3))
