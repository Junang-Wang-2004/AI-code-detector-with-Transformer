class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        ans = 0
        for sx in (1, -1):
            for sy in (1, -1):
                min_so_far = float('inf')
                for pos, x, y in zip(range(len(arr1)), arr1, arr2):
                    val = sx * x + sy * y + pos
                    ans = max(ans, val - min_so_far)
                    min_so_far = min(min_so_far, val)
        return ans
