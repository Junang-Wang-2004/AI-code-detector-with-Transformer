class Solution:
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        cuts = [(c, 0) for c in horizontalCut] + [(c, 1) for c in verticalCut]
        cuts.sort(reverse=True)
        done_h = done_v = 0
        total = 0
        for c, typ in cuts:
            if typ == 0:
                total += c * (done_v + 1)
                done_h += 1
            else:
                total += c * (done_h + 1)
                done_v += 1
        return total
