class Solution:
    def insert(self, inters, ni):
        l, r = 0, 0
        n = len(inters)
        st, en = ni
        while l < n and inters[l][1] < st:
            l += 1
        r = l
        while r < n and inters[r][0] <= en:
            st = min(st, inters[r][0])
            en = max(en, inters[r][1])
            r += 1
        return inters[:l] + [[st, en]] + inters[r:]
