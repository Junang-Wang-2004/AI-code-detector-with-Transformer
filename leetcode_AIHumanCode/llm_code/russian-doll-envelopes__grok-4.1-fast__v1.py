class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        seq = sorted(envelopes, key=lambda p: (p[0], -p[1]))
        tails = []
        def search(val):
            lo, hi = 0, len(tails)
            while lo < hi:
                md = (lo + hi) // 2
                if tails[md] < val:
                    lo = md + 1
                else:
                    hi = md
            return lo
        for _, ht in seq:
            idx = search(ht)
            if idx == len(tails):
                tails.append(ht)
            else:
                tails[idx] = ht
        return len(tails)
