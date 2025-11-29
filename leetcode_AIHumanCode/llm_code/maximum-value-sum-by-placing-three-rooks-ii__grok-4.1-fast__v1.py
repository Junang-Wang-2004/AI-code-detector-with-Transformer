class Solution(object):
    def maximumValueSum(self, board):
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        k = 3
        row_candidates = set()
        for i in range(m):
            row_list = [(board[i][j], i, j) for j in range(n)]
            top_row = sorted(row_list, reverse=True)[:k]
            for item in top_row:
                row_candidates.add(item)
        col_candidates = set()
        for j in range(n):
            col_list = [(board[i][j], i, j) for i in range(m)]
            top_col = sorted(col_list, reverse=True)[:k]
            for item in top_col:
                col_candidates.add(item)
        promising = row_candidates & col_candidates
        cell_list = sorted(promising, reverse=True)
        num_needed = (k - 1) * (2 * k - 1) + 1
        cells = cell_list[:num_needed]
        row_mask = [False] * m
        col_mask = [False] * n
        res = float('-inf')

        def search(start, picks, current_sum):
            nonlocal res
            if picks == k:
                res = max(res, current_sum)
                return
            for idx in range(start, len(cells)):
                value, r, c = cells[idx]
                if row_mask[r] or col_mask[c]:
                    continue
                row_mask[r] = True
                col_mask[c] = True
                search(idx + 1, picks + 1, current_sum + value)
                row_mask[r] = False
                col_mask[c] = False

        search(0, 0, 0)
        return res
