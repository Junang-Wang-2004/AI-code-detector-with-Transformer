from functools import lru_cache

class C1:

    def countSteppingNumbers(self, a1, a2):
        v1 = 10 ** 9 + 7

        def digit_dp(a1):
            v1 = str(a1)
            v2 = len(v1)

            @lru_cache(None)
            def dfs(a1, a2, a3, a4):
                if a1 == v2:
                    return 1 if not a4 else 0
                v1 = 0
                v2 = int(v1[a1]) if a2 else 9
                for v3 in range(v2 + 1):
                    v4 = 1 if a2 and v3 == v2 else 0
                    if a4 and v3 == 0:
                        v1 = (v1 + dfs(a1 + 1, v4, -1, 1)) % v1
                    else:
                        v5 = v3
                        if not a4 and abs(v3 - a3) != 1:
                            continue
                        v1 = (v1 + dfs(a1 + 1, v4, v5, 0)) % v1
                return v1
            return dfs(0, 1, -1, 1)
        return (digit_dp(a2) - digit_dp(a1 - 1) + v1) % v1
