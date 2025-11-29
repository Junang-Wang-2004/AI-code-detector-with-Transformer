import functools

class C1:

    def numberOfBeautifulIntegers(self, a1: int, a2: int, a3: int) -> int:

        def process(a1: int, a2: int) -> int:
            if a1 <= 0:
                return 0
            v1 = str(a1)
            v2 = len(v1)
            v3 = tuple((int(c) for v4 in v1))

            @functools.lru_cache(None)
            def rec(a1: int, a2: bool, a3: bool, a4: int, a5: int) -> int:
                if a1 == v2:
                    return int(not a2 and a4 == 0 and (a5 == 0))
                v1 = 0
                v2 = v3[a1] if a3 else 9
                for v3 in range(v2 + 1):
                    v4 = a2 and v3 == 0
                    v5 = a3 and v3 == v2
                    v6 = (a5 * 10 + v3) % a2
                    v7 = a4
                    if not v4:
                        v7 += 1 if v3 % 2 == 0 else -1
                    v1 += rec(a1 + 1, v4, v5, v7, v6)
                return v1
            return rec(0, True, True, 0, 0)
        return process(a2, a3) - process(a1 - 1, a3)
