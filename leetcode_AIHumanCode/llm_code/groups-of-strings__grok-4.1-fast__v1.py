from collections import Counter

class Solution:
    def groupStrings(self, words):
        cnt = Counter()
        for s in words:
            msk = 0
            for ch in s:
                msk |= 1 << (ord(ch) - ord('a'))
            cnt[msk] += 1
        msks = list(cnt)
        nm = len(msks)
        idmap = {msks[j]: j for j in range(nm)}
        class DSU:
            def __init__(self, sz):
                self.pr = list(range(sz))
                self.rk = [0] * sz
                self.sz = [cnt[msks[j]] for j in range(sz)]
            def get(self, x):
                if self.pr[x] != x:
                    self.pr[x] = self.get(self.pr[x])
                return self.pr[x]
            def merge(self, x, y):
                px = self.get(x)
                py = self.get(y)
                if px == py:
                    return
                if self.rk[px] < self.rk[py]:
                    self.pr[px] = py
                    self.sz[py] += self.sz[px]
                elif self.rk[px] > self.rk[py]:
                    self.pr[py] = px
                    self.sz[px] += self.sz[py]
                else:
                    self.pr[py] = px
                    self.sz[px] += self.sz[py]
                    self.rk[px] += 1
        if nm == 0:
            return [0, 0]
        uf = DSU(nm)
        for i in range(nm):
            cm = msks[i]
            for k in range(26):
                bt = 1 << k
                if cm & bt:
                    sm = cm ^ bt
                    if sm in idmap:
                        uf.merge(i, idmap[sm])
        visited = set()
        grps = 0
        mxsz = 0
        for i in range(nm):
            rt = uf.get(i)
            if rt not in visited:
                visited.add(rt)
                grps += 1
                mxsz = max(mxsz, uf.sz[rt])
        return [grps, mxsz]
