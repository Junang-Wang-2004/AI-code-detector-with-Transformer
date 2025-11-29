class Solution:
    def visibleMountains(self, peaks):
        peaks.sort(key=lambda p: p[0] - p[1])
        res = 0
        best = 0
        idx = 0
        m = len(peaks)
        while idx < m:
            diff = peaks[idx][0] - peaks[idx][1]
            gmax = 0
            while idx < m and peaks[idx][0] - peaks[idx][1] == diff:
                sm = peaks[idx][0] + peaks[idx][1]
                if sm > gmax:
                    gmax = sm
                idx += 1
            if gmax > best:
                res += 1
                best = gmax
        return res
