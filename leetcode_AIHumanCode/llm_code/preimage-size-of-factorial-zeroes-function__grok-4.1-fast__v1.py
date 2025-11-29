class Solution:
    def preimageSizeFZF(self, K):
        def zeros(n):
            total = 0
            while n:
                n //= 5
                total += n
            return total

        def first_ge(val):
            l, r = 0, 5 * (val + 1)
            while l < r:
                mid = (l + r) // 2
                if zeros(mid) >= val:
                    r = mid
                else:
                    l = mid + 1
            return l

        begin = first_ge(K)
        finish = first_ge(K + 1) - 1
        if zeros(begin) != K:
            return 0
        return finish - begin + 1
