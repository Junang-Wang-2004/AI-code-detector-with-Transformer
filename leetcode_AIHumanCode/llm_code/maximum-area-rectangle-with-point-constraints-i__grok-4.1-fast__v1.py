class Solution:
    def maxRectangleArea(self, points):
        points.sort()
        all_y = sorted({p[1] for p in points})
        y_rank = {y: i+1 for i, y in enumerate(all_y)}
        m = len(all_y)
        fen = [0] * (m + 2)
        def add(pos, delta):
            while pos <= m:
                fen[pos] += delta
                pos += pos & -pos
        def sum_upto(pos):
            total = 0
            while pos > 0:
                total += fen[pos]
                pos -= pos & -pos
            return total
        record = {}
        ans = -1
        i = 0
        npts = len(points)
        while i < npts:
            x_now = points[i][0]
            j = i
            while j < npts and points[j][0] == x_now:
                j += 1
            for k in range(i, j):
                add(y_rank[points[k][1]], 1)
            for k in range(i, j-1):
                bot_y = points[k][1]
                top_y = points[k+1][1]
                b_idx = y_rank[bot_y]
                t_idx = y_rank[top_y]
                cnt_cur = sum_upto(t_idx) - sum_upto(b_idx - 1)
                pair = (b_idx, t_idx)
                if pair in record:
                    prev_cnt, prev_x = record[pair]
                    if prev_cnt + 2 == cnt_cur:
                        area = (x_now - prev_x) * (top_y - bot_y)
                        ans = max(ans, area)
                record[pair] = (cnt_cur, x_now)
            i = j
        return ans
