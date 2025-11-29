class Solution:
    def minimumSum(self, grid):
        n, m = len(grid), len(grid[0])
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = grid[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j]

        def range_query(x1, y1, x2, y2):
            return (pref[x2 + 1][y2 + 1] - pref[x2 + 1][y1] - pref[x1][y2 + 1] + pref[x1][y1])

        def first_row_with_one(r_start, r_end, c_start, c_end):
            lo, hi = r_start, r_end
            while lo <= hi:
                md = (lo + hi) // 2
                if range_query(r_start, c_start, md, c_end) > 0:
                    hi = md - 1
                else:
                    lo = md + 1
            return lo if lo <= r_end and range_query(r_start, c_start, lo, c_end) > 0 else r_end + 1

        def last_row_with_one(r_start, r_end, c_start, c_end):
            lo, hi = r_start, r_end
            while lo <= hi:
                md = (lo + hi) // 2
                if range_query(md, c_start, r_end, c_end) > 0:
                    lo = md + 1
                else:
                    hi = md - 1
            return hi if hi >= r_start and range_query(hi, c_start, r_end, c_end) > 0 else r_start - 1

        def first_col_with_one(r_start, r_end, c_start, c_end):
            lo, hi = c_start, c_end
            while lo <= hi:
                md = (lo + hi) // 2
                if range_query(r_start, c_start, r_end, md) > 0:
                    hi = md - 1
                else:
                    lo = md + 1
            return lo if lo <= c_end and range_query(r_start, c_start, r_end, lo) > 0 else c_end + 1

        def last_col_with_one(r_start, r_end, c_start, c_end):
            lo, hi = c_start, c_end
            while lo <= hi:
                md = (lo + hi) // 2
                if range_query(r_start, md, r_end, c_end) > 0:
                    lo = md + 1
                else:
                    hi = md - 1
            return hi if hi >= c_start and range_query(r_start, hi, r_end, c_end) > 0 else c_start - 1

        def bounding_area(r1, r2, c1, c2):
            if r1 > r2 or c1 > c2:
                return 0
            min_row = first_row_with_one(r1, r2, c1, c2)
            max_row = last_row_with_one(r1, r2, c1, c2)
            min_col = first_col_with_one(r1, r2, c1, c2)
            max_col = last_col_with_one(r1, r2, c1, c2)
            if min_row > max_row or min_col > max_col:
                return 0
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        res = float('inf')

        for cut_row in range(n - 1):
            bot = bounding_area(cut_row + 1, n - 1, 0, m - 1)
            for cut_col in range(m - 1):
                top_l = bounding_area(0, cut_row, 0, cut_col)
                top_r = bounding_area(0, cut_row, cut_col + 1, m - 1)
                res = min(res, top_l + top_r + bot)

        for cut_row in range(n - 1):
            top = bounding_area(0, cut_row, 0, m - 1)
            for cut_col in range(m - 1):
                bot_l = bounding_area(cut_row + 1, n - 1, 0, cut_col)
                bot_r = bounding_area(cut_row + 1, n - 1, cut_col + 1, m - 1)
                res = min(res, top + bot_l + bot_r)

        for cut_col in range(m - 1):
            right =
