class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        excavated = set((r, c) for r, c in dig)
        total = 0
        for bounds in artifacts:
            start_row, start_col, end_row, end_col = bounds
            complete = True
            for row in range(start_row, end_row + 1):
                if not complete:
                    break
                for col in range(start_col, end_col + 1):
                    if (row, col) not in excavated:
                        complete = False
                        break
            if complete:
                total += 1
        return total
