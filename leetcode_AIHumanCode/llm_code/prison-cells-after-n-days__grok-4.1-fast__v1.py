class Solution(object):
    def prisonAfterNDays(self, cells, N):
        def nxt(st):
            return tuple([0] + [int(st[i-1] == st[i+1]) for i in range(1, 7)] + [0])
        if N == 0:
            return cells[:]
        seen = {}
        st = tuple(cells)
        d = 0
        while d < N:
            if st in seen:
                break
            seen[st] = d
            st = nxt(st)
            d += 1
        else:
            return list(st)
        cyc_start = seen[st]
        cyc_len = d - cyc_start
        eff_d = cyc_start + (N - cyc_start) % cyc_len
        st = tuple(cells)
        for _ in range(eff_d):
            st = nxt(st)
        return list(st)
