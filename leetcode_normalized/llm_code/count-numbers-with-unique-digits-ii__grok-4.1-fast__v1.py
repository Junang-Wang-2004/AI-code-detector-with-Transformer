class C1:

    def numberCount(self, a1, a2):

        def count(a1):
            if a1 < 0:
                return 0
            v1 = str(a1)
            v2 = len(v1)
            from functools import lru_cache

            @lru_cache(None)
            def dfs(a1, a2, a3, a4):
                if a1 == v2:
                    return 1
                v1 = 0
                v2 = int(v1[a1]) if a3 else 9
                for v3 in range(v2 + 1):
                    v4 = 1 if a3 and v3 == v2 else 0
                    if a4 and v3 == 0:
                        v1 += dfs(a1 + 1, 0, v4, 1)
                        continue
                    v5 = 0
                    if a4:
                        v6 = 1 << v3
                    else:
                        if a2 & 1 << v3:
                            continue
                        v6 = a2 | 1 << v3
                    v1 += dfs(a1 + 1, v6, v4, v5)
                return v1
            return dfs(0, 0, 1, 1)
        return count(a2) - count(a1 - 1)
