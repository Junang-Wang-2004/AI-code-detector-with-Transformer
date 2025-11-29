class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        trailing = []
        for row in grid:
            cnt = 0
            while cnt < n and row[n - 1 - cnt] == 0:
                cnt += 1
            trailing.append(cnt)
        ans = 0
        for pos in range(n - 1):
            req = n - 1 - pos
            found = next((i for i in range(pos, n) if trailing[i] >= req), -1)
            if found == -1:
                return -1
            ans += found - pos
            val = trailing.pop(found)
            trailing.insert(pos, val)
        return ans
