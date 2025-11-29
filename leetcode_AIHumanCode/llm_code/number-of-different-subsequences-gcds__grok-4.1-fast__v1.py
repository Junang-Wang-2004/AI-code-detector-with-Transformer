import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums):
        mx = max(nums)
        has_num = [False] * (mx + 1)
        for val in nums:
            has_num[val] = True
        total = 0
        for target in range(1, mx + 1):
            cg = 0
            step = target
            while step <= mx:
                if has_num[step]:
                    cg = math.gcd(cg, step)
                    if cg == target:
                        total += 1
                        break
                step += target
        return total
