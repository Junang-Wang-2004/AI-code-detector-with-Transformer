from functools import lru_cache

class C1:

    def count(self, a1: str, a2: str, a3: int, a4: int) -> int:
        v1 = 10 ** 9 + 7

        def numbers_up_to(a1: str, a2: int, a3: int) -> int:
            if int(a1) < 0:
                return 0
            v1 = tuple((int(ch) for v2 in a1))
            v3 = len(v1)

            @lru_cache(None)
            def rec(a1: int, a2: int, a3: bool) -> int:
                if a1 == v3:
                    return 1 if a2 <= a2 <= a3 else 0
                v1 = 0
                v2 = v1[a1] if a3 else 9
                for v3 in range(v2 + 1):
                    v4 = a2 + v3
                    if v4 > a3:
                        continue
                    v5 = a3 and v3 == v2
                    v1 = (v1 + rec(a1 + 1, v4, v5)) % v1
                return v1
            return rec(0, 0, True)
        v2 = str(int(a1) - 1)
        v3 = (numbers_up_to(a2, a3, a4) - numbers_up_to(v2, a3, a4) + v1) % v1
        return v3
