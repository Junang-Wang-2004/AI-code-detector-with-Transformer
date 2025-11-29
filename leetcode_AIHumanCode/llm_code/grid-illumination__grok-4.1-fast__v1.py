import collections

class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        active = set()
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        mains = collections.defaultdict(int)
        antis = collections.defaultdict(int)
        
        for pos in lamps:
            i, j = pos
            p = (i, j)
            if p in active:
                continue
            active.add(p)
            rows[i] += 1
            cols[j] += 1
            mains[i - j] += 1
            antis[i + j] += 1
        
        res = []
        for q in queries:
            qi, qj = q
            keym = qi - qj
            keya = qi + qj
            illum = rows[qi] or cols[qj] or mains[keym] or antis[keya]
            if not illum:
                res.append(0)
                continue
            res.append(1)
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni = qi + di
                    nj = qj + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        np = (ni, nj)
                        if np in active:
                            active.discard(np)
                            rows[ni] -= 1
                            cols[nj] -= 1
                            mains[ni - nj] -= 1
                            antis[ni + nj] -= 1
        return res
