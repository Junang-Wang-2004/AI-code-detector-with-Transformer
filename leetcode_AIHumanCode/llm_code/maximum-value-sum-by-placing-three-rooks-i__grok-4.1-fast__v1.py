class Solution:
    def maximumValueSum(self, board):
        k = 3
        rows_count = len(board)
        cols_count = len(board[0])
        row_best = []
        for row_idx in range(rows_count):
            entries = [(board[row_idx][col_idx], row_idx, col_idx) for col_idx in range(cols_count)]
            entries.sort(key=lambda x: x[0], reverse=True)
            row_best.append(entries[:k])
        col_best = [[] for _ in range(cols_count)]
        for best_in_row in row_best:
            for entry in best_in_row:
                col_idx = entry[2]
                col_best[col_idx].append(entry)
        for col_idx in range(cols_count):
            col_best[col_idx].sort(key=lambda x: x[0], reverse=True)
            col_best[col_idx] = col_best[col_idx][:k]
        all_entries = []
        for lst in col_best:
            all_entries.extend(lst)
        all_entries.sort(key=lambda x: x[0], reverse=True)
        needed = (k - 1) * (2 * k - 1) + 1
        shortlist = all_entries[:needed]
        ans = 0
        sl_len = len(shortlist)
        for idx1 in range(sl_len):
            val1, row1, col1 = shortlist[idx1]
            for idx2 in range(idx1 + 1, sl_len):
                val2, row2, col2 = shortlist[idx2]
                if row1 == row2 or col1 == col2:
                    continue
                for idx3 in range(idx2 + 1, sl_len):
                    val3, row3, col3 = shortlist[idx3]
                    if row3 == row1 or row3 == row2 or col3 == col1 or col3 == col2:
                        continue
                    ans = max(ans, val1 + val2 + val3)
        return ans
