class Solution(object):
    def maxIntersectionCount(self, y):
        pos_delta = {}
        n = len(y)
        for i in range(n - 1):
            a = y[i]
            b = y[i + 1]
            lft = 2 * a
            rgt = 2 * b + (-1 if a < b else 1)
            st = min(lft, rgt)
            en = max(lft, rgt) + 1
            pos_delta[st] = pos_delta.get(st, 0) + 1
            pos_delta[en] = pos_delta.get(en, 0) - 1
        lst = y[n - 1]
        st = 2 * lst
        en = st + 1
        pos_delta[st] = pos_delta.get(st, 0) + 1
        pos_delta[en] = pos_delta.get(en, 0) - 1
        pts = sorted(pos_delta)
        cur = 0
        mx = 0
        for p in pts:
            cur += pos_delta[p]
            if cur > mx:
                mx = cur
        return mx
