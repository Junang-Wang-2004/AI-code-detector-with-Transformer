import collections

class Solution(object):
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        h, w = min(m, n), max(m, n)
        if h == 0:
            return 1

        def get_valid_masks(height):
            masks = [0]
            power = 1
            for _ in range(height):
                new_masks = []
                for mask in masks:
                    prev_c = (mask // (power // 3)) % 3 if power > 1 else -1
                    for c in range(3):
                        if c == prev_c:
                            continue
                        new_masks.append(mask + c * power)
                masks = new_masks
                power *= 3
            return masks

        def get_compat_curr(height, prev_mask):
            masks = [0]
            power = 1
            for pos in range(height):
                new_masks = []
                for mask in masks:
                    prev_c_col = (mask // (power // 3)) % 3 if power > 1 else -1
                    forbid_v = (prev_mask // power) % 3
                    for c in range(3):
                        if c == prev_c_col or c == forbid_v:
                            continue
                        new_masks.append(mask + c * power)
                masks = new_masks
                power *= 3
            return masks

        def get_canon(height, mask):
            color_map = {}
            nid = 0
            res = 0
            power = 1
            for _ in range(height):
                col = (mask // power) % 3
                if col not in color_map:
                    color_map[col] = nid
                    nid += 1
                res += color_map[col] * power
                power *= 3
            return res

        raw_masks = get_valid_masks(h)
        norm_cnt = collections.Counter(get_canon(h, rm) for rm in raw_masks)
        if w == 1:
            return sum(norm_cnt.values()) % MOD

        states = sorted(norm_cnt)
        ns = len(states)
        idx_map = {states[i]: i for i in range(ns)}
        adj_mat = [[0] * ns for _ in range(ns)]
        for i in range(ns):
            p_rep = states[i]
            next_raws = get_compat_curr(h, p_rep)
            tgt_cnts = collections.Counter(get_canon(h, nr) for nr in next_raws)
            for tgt, ct in tgt_cnts.items():
                j = idx_map[tgt]
                adj_mat[i][j] = ct % MOD

        def matrix_multiply(x, y, md):
            rx, cx = len(x), len(x[0])
            cy = len(y[0])
            z = [[0] * cy for _ in range(rx)]
            for i in range(rx):
                for k in range(cx):
                    if x[i][k] == 0:
                        continue
                    val = x[i][k]
                    for j in range(cy):
                        z[i][j] = (z[i][j] + val * y[k][j]) % md
            return z

        def matrix_power(base, ex, md):
            sz = len(base)
            rst = [[1 if ii == jj else 0 for jj in range(sz)] for ii in range(sz)]
            while ex > 0:
                if ex & 1:
                    rst = matrix_multiply(rst, base, md)
                base = matrix_multiply(base, base, md)
                ex >>= 1
            return rst

        init_row = [[norm_cnt[states[i]] for i in range(ns)]]
        trans_pow = matrix_power(adj_mat, w - 1, MOD)
        final_row = matrix_multiply(init_row, trans_pow, MOD)
        return sum(final_row[0]) % MOD
