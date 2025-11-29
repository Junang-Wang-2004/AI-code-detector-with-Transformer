class Solution(object):
    def matrixSumQueries(self, n, queries):
        row_visited = [False] * n
        col_visited = [False] * n
        active_rows = 0
        active_cols = 0
        total = 0
        for op_type, pos, amt in reversed(queries):
            if op_type == 0:
                if row_visited[pos]:
                    continue
                row_visited[pos] = True
                active_rows += 1
                total += amt * (n - active_cols)
            else:
                if col_visited[pos]:
                    continue
                col_visited[pos] = True
                active_cols += 1
                total += amt * (n - active_rows)
        return total
