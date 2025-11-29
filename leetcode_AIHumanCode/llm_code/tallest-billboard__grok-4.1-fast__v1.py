class Solution(object):
    def tallestBillboard(self, rods):
        n = len(rods)
        mid = n // 2
        g1 = rods[:mid]
        g2 = rods[mid:]

        def process(group):
            mp = {0: 0}
            for r in group:
                nxt = mp.copy()
                for dif, h in mp.items():
                    ndif1 = dif + r
                    nxt[ndif1] = max(nxt.get(ndif1, 0), h)
                    ndif2 = abs(dif - r)
                    nh2 = h + min(dif, r)
                    nxt[ndif2] = max(nxt.get(ndif2, 0), nh2)
                mp = nxt
            return mp

        m1 = process(g1)
        m2 = process(g2)
        res = 0
        for dif in m1:
            if dif in m2:
                res = max(res, m1[dif] + m2[dif] + dif)
        return res
