class Solution:
    def permute(self, n, k):
        fac = [1] * (n // 2 + 2)
        for i in range(1, len(fac)):
            fac[i] = fac[i - 1] * i
        used = [False] * n
        res = []
        rk = k
        for p in range(n):
            rl = n - p - 1
            wc = fac[rl // 2] * fac[(rl + 1) // 2]
            req_odd = None
            if p > 0:
                prev = res[-1]
                req_odd = (prev % 2 == 0)
            elif n % 2 == 1:
                req_odd = True
            selected = False
            for num in range(1, n + 1):
                j = num - 1
                if used[j]:
                    continue
                odd_flag = (num % 2 == 1)
                if req_odd is not None and odd_flag != req_odd:
                    continue
                if rk <= wc:
                    used[j] = True
                    res.append(num)
                    selected = True
                    break
                rk -= wc
            if not selected:
                return []
        return res
