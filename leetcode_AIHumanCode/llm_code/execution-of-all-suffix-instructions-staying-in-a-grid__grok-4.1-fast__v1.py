import collections

class Solution(object):
    def executeInstructions(self, n, startPos, s):
        dirs_row = {'U': -1, 'R': 0, 'D': 1, 'L': 0}
        dirs_col = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
        sr, sc = startPos
        m = len(s)
        row_ds = [dirs_row[ch] for ch in s]
        col_ds = [dirs_col[ch] for ch in s]
        row_max = self._get_limits(n, sr, row_ds)
        col_max = self._get_limits(n, sc, col_ds)
        return [min(row_max[i], col_max[i]) for i in range(m)]

    def _get_limits(self, n, start, ds):
        m = len(ds)
        limits = list(range(m, 0, -1))
        pos_map = collections.defaultdict(list)
        cpos = 0
        pos_map[start - cpos].append(0)
        for idx in range(m):
            cpos += ds[idx]
            for barrier in (n - cpos, -cpos - 1):
                if barrier in pos_map:
                    for st in pos_map[barrier]:
                        limits[st] = min(limits[st], idx - st)
                    pos_map[barrier] = []
            pos_map[start - cpos].append(idx + 1)
        return limits
