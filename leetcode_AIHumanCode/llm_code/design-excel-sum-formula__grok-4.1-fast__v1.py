import collections

class Excel:

    def __init__(self, H, W):
        nc = ord(W) - ord('A') + 1
        self.cells = [[0] * nc for _ in range(H + 1)]
        self.outgoing = collections.defaultdict(lambda: collections.defaultdict(int))
        self.incoming = collections.defaultdict(set)

    def set(self, r, c, v):
        ci = ord(c) - ord('A')
        self._unlink(r, ci)
        old = self.cells[r][ci]
        self.cells[r][ci] = v
        self._ripple(r, ci, v - old)

    def get(self, r, c):
        return self.cells[r][ord(c) - ord('A')]

    def sum(self, r, c, formulas):
        ci = ord(c) - ord('A')
        self._unlink(r, ci)
        tot = 0
        rels = set()
        for spec in formulas:
            bits = spec.split(':')
            fr = bits[0]
            to = bits[1] if len(bits) > 1 else fr
            c1 = ord(fr[0]) - ord('A')
            r1 = int(fr[1:])
            c2 = ord(to[0]) - ord('A')
            r2 = int(to[1:])
            for rr in range(r1, r2 + 1):
                for cc in range(c1, c2 + 1):
                    tot += self.cells[rr][cc]
                    src = (rr, cc)
                    self.outgoing[src][(r, ci)] += 1
                    rels.add(src)
        self.incoming[(r, ci)] = rels
        old = self.cells[r][ci]
        self.cells[r][ci] = tot
        self._ripple(r, ci, tot - old)
        return tot

    def _unlink(self, r, ci):
        targets = self.incoming[(r, ci)]
        for sr, sc in targets:
            self.outgoing[(sr, sc)].pop((r, ci), None)
        self.incoming[(r, ci)].clear()

    def _ripple(self, r, ci, delta):
        if not delta:
            return
        q = collections.deque([((r, ci), delta)])
        while q:
            pos, d = q.popleft()
            for tgt, mul in self.outgoing[pos].items():
                nd = d * mul
                tr, tc = tgt
                self.cells[tr][tc] += nd
                q.append((tgt, nd))
