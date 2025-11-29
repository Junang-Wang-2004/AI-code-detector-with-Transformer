class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        cells = m * n
        occupancy = [0] * cells
        best = [0]

        def compute_delta(typ: int, left_nb: int, up_nb: int) -> int:
            old_adjust = -30 * ((left_nb == 1) + (up_nb == 1)) + 20 * ((left_nb == 2) + (up_nb == 2))
            adj_count = (left_nb != 0) + (up_nb != 0)
            if typ == 1:
                return old_adjust + 120 - 30 * adj_count
            if typ == 2:
                return old_adjust + 40 + 20 * adj_count
            return 0

        def search(pos: int, i_left: int, e_left: int, score: int):
            if pos == cells or (i_left == 0 and e_left == 0):
                best[0] = max(best[0], score)
                return
            if score + 120 * (i_left + e_left) < best[0]:
                return
            l_idx = pos - 1 if pos % n else -1
            u_idx = pos - n if pos >= n else -1
            l_nb = occupancy[l_idx] if l_idx >= 0 else 0
            u_nb = occupancy[u_idx] if u_idx >= 0 else 0
            has_adj = l_nb or u_nb
            if i_left > 0:
                delta = compute_delta(1, l_nb, u_nb)
                occupancy[pos] = 1
                search(pos + 1, i_left - 1, e_left, score + delta)
                occupancy[pos] = 0
            if e_left > 0:
                delta = compute_delta(2, l_nb, u_nb)
                occupancy[pos] = 2
                search(pos + 1, i_left, e_left - 1, score + delta)
                occupancy[pos] = 0
            if has_adj:
                search(pos + 1, i_left, e_left, score)

        search(0, introvertsCount, extrovertsCount, 0)
        return best[0]
