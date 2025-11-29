import functools

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def process(limit: int, k: int) -> int:
            if limit <= 0:
                return 0
            s = str(limit)
            n = len(s)
            digs = tuple(int(c) for c in s)

            @functools.lru_cache(None)
            def rec(idx: int, leadz: bool, lim: bool, dif: int, md: int) -> int:
                if idx == n:
                    return int(not leadz and dif == 0 and md == 0)
                res = 0
                hi = digs[idx] if lim else 9
                for d in range(hi + 1):
                    nzlead = leadz and d == 0
                    nlim = lim and d == hi
                    nmd = (md * 10 + d) % k
                    ndif = dif
                    if not nzlead:
                        ndif += 1 if d % 2 == 0 else -1
                    res += rec(idx + 1, nzlead, nlim, ndif, nmd)
                return res

            return rec(0, True, True, 0, 0)

        return process(high, k) - process(low - 1, k)
