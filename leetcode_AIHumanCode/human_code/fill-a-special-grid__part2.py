# Time:  O(4^n)
# Space: O(n)
# divide and conquer
class Solution2(object):
    def specialGrid(self, n):
        """
        """
        def divide_and_conquer(l, r, c):
            if l == 1:
                result[r][c] = idx[0]
                idx[0] += 1
                return
            l >>= 1
            for dr, dc in ((0, l), (l, 0), (0, -l), (-l, 0)):
                r, c = r+dr, c+dc
                divide_and_conquer(l, r, c)

        total = 1<<n
        result = [[0]*total for _ in range(total)]
        idx = [0]
        divide_and_conquer(total, 0, 0)
        return result
