class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        n = len(prefix)

        def divide_conquer(l, r, lo, hi):
            if r - l <= 1:
                return 0
            m = l + (r - l) // 2
            res = divide_conquer(l, m, lo, hi) + divide_conquer(m, r, lo, hi)
            buf = []
            p1, p2, p3 = m, m, m
            for i in range(l, m):
                while p1 < r and prefix[p1] - prefix[i] < lo:
                    p1 += 1
                while p2 < r and prefix[p2] - prefix[i] <= hi:
                    p2 += 1
                res += p2 - p1
                while p3 < r and prefix[p3] < prefix[i]:
                    buf.append(prefix[p3])
                    p3 += 1
                buf.append(prefix[i])
            while p3 < r:
                buf.append(prefix[p3])
                p3 += 1
            prefix[l:r] = buf
            return res

        return divide_conquer(0, n, lower, upper)
