class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        rminc = {}
        rmaxc = {}
        cminr = {}
        cmaxr = {}
        for b in buildings:
            cx, ry = b[0] - 1, b[1] - 1
            rminc[ry] = min(rminc.get(ry, n), cx)
            rmaxc[ry] = max(rmaxc.get(ry, -1), cx)
            cminr[cx] = min(cminr.get(cx, n), ry)
            cmaxr[cx] = max(cmaxr.get(cx, -1), ry)
        res = 0
        for b in buildings:
            cx, ry = b[0] - 1, b[1] - 1
            if rminc[ry] < cx < rmaxc[ry] and cminr[cx] < ry < cmaxr[cx]:
                res += 1
        return res
