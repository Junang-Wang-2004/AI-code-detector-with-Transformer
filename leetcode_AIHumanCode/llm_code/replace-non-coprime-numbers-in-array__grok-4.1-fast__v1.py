class Solution:
    def replaceNonCoprimes(self, nums):
        def gcd(p, q):
            while q != 0:
                p, q = q, p % q
            return p

        stk = []
        for n in nums:
            stk.append(n)
            while len(stk) > 1:
                x = stk[-2]
                y = stk[-1]
                d = gcd(x, y)
                if d == 1:
                    break
                stk.pop()
                stk.pop()
                stk.append(y * (x // d))
        return stk
