class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        availA = sorted(slots1)
        availB = sorted(slots2)
        p, q = 0, 0
        while p < len(availA) and q < len(availB):
            ostart = max(availA[p][0], availB[q][0])
            oend = min(availA[p][1], availB[q][1])
            if oend - ostart >= duration:
                return [ostart, ostart + duration]
            if availA[p][1] <= availB[q][1]:
                p += 1
            else:
                q += 1
        return []
