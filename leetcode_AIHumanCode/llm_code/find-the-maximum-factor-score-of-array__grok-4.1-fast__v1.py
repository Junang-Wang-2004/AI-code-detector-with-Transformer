class Solution(object):
    def maxScore(self, nums):
        def gcd(a, b):
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a

        def lcm(a, b):
            g = gcd(a, b)
            return a // g * b if g != 0 else 0

        n = len(nums)
        if n == 0:
            return 0
        pg = [0] * n
        pl = [0] * n
        pg[0] = nums[0]
        pl[0] = nums[0]
        for k in range(1, n):
            pg[k] = gcd(pg[k - 1], nums[k])
            pl[k] = lcm(pl[k - 1], nums[k])
        sg = [0] * n
        sl = [0] * n
        sg[n - 1] = nums[n - 1]
        sl[n - 1] = nums[n - 1]
        for k in range(n - 2, -1, -1):
            sg[k] = gcd(nums[k], sg[k + 1])
            sl[k] = lcm(nums[k], sl[k + 1])
        mx = pg[n - 1] * pl[n - 1]
        for i in range(n):
            leftg = pg[i - 1] if i > 0 else 0
            rightg = sg[i + 1] if i + 1 < n else 0
            exg = gcd(leftg, rightg)
            leftl = pl[i - 1] if i > 0 else 1
            rightl = sl[i + 1] if i + 1 < n else 1
            exl = lcm(leftl, rightl)
            mx = max(mx, exg * exl)
        return mx
