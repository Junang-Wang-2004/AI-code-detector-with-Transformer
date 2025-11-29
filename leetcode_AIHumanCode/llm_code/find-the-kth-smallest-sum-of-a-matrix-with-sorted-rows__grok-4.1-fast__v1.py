class Solution:
    def kthSmallest(self, mat, k):
        def combos_le(rows, max_k, cur_row, rem_sum):
            if cur_row == len(rows):
                return 1
            total = 0
            n_cols = len(rows[0])
            for col in range(n_cols):
                next_sum = rem_sum - rows[cur_row][col]
                if next_sum < 0:
                    break
                sub_total = combos_le(rows, max_k - total, cur_row + 1, next_sum)
                if sub_total == 0:
                    break
                total += sub_total
                if total >= max_k:
                    return max_k
            return total

        num_rows = len(mat)
        low = sum(row[0] for row in mat)
        high = sum(row[-1] for row in mat)
        while low < high:
            mid_val = low + (high - low) // 2
            if combos_le(mat, k, 0, mid_val) >= k:
                high = mid_val
            else:
                low = mid_val + 1
        return low
