class Solution(object):
    def closestFair(self, n):
        s = str(n)
        ld = len(s)
        ds = [int(c) for c in s]
        ans_ds = None
        if ld % 2 == 0:
            h = ld // 2
            ev_cnt = sum(d % 2 == 0 for d in ds)
            if ev_cnt == h:
                return n
            par_cnt = [0, 0]
            for d in ds:
                par_cnt[d % 2] += 1
            for i in range(ld - 1, h - 1, -1):
                old_par = ds[i] % 2
                par_cnt[old_par] -= 1
                req = [h - par_cnt[0], h - par_cnt[1]]
                if min(req) < 0:
                    continue
                old_d = ds[i]
                cand = old_d + 1
                p = cand % 2
                if cand <= 9 and req[p] >= 1:
                    req[p] -= 1
                    ans_ds = ds[:i] + [cand] + [0] * req[0] + [1] * req[1]
                    break
                cand = old_d + 2
                p = cand % 2
                if cand <= 9 and req[p] >= 1:
                    req[p] -= 1
                    ans_ds = ds[:i] + [cand] + [0] * req[0] + [1] * req[1]
                    break
        if ans_ds is None:
            hh = ld // 2 + 1
            ans_ds = [1] + [0] * hh + [1] * (hh - 1)
        return int(''.join(str(d) for d in ans_ds))
