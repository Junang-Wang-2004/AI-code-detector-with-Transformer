class Solution:
    def findSolution(self, customfunction, z):
        ans = []
        max_x = 1
        while customfunction.f(max_x, 1) < z:
            max_x += 1
        max_y = 1
        while customfunction.f(1, max_y) < z:
            max_y += 1
        for x in range(1, max_x + 1):
            lo, hi = 1, max_y
            while lo <= hi:
                mid = (lo + hi) // 2
                val = customfunction.f(x, mid)
                if val == z:
                    ans.append([x, mid])
                    break
                elif val < z:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return ans
