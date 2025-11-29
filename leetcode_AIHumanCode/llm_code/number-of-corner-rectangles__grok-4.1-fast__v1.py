class Solution(object):
    def countCornerRectangles(self, grid):
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        cols_with_ones = [[] for _ in range(w)]
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    cols_with_ones[j].append(i)
        ans = 0
        def intersect_size(a, b):
            p1 = p2 = 0
            matches = 0
            while p1 < len(a) and p2 < len(b):
                if a[p1] == b[p2]:
                    matches += 1
                    p1 += 1
                    p2 += 1
                elif a[p1] < b[p2]:
                    p1 += 1
                else:
                    p2 += 1
            return matches
        for x in range(w):
            for y in range(x):
                k = intersect_size(cols_with_ones[x], cols_with_ones[y])
                ans += k * (k - 1) // 2
        return ans
