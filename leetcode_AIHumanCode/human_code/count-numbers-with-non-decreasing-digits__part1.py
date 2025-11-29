# Time:  O(n^2), n = len(r)
# Space: O(n)

# math, stars and bars, combinatorics
class Solution(object):
    def countNumbers(self, l, r, b):
        """
        """
        MOD = 10**9+7
        fact, inv, inv_fact = [[1]*2 for _ in range(3)]
        def nCr(n, k):
            while len(inv) <= n:  # lazy initialization
                fact.append(fact[-1]*len(inv) % MOD)
                inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
                inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
            return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

        def nHr(n, k):
            return nCr(n+k-1, k)

        def count(x):
            digits_base = []
            while x:
                x, r = divmod(x, b)
                digits_base.append(r)
            digits_base.reverse()
            if not digits_base:
                digits_base.append(0)
            result = 0
            for i in range(len(digits_base)):
                if i-1 >= 0 and digits_base[i-1] > digits_base[i]:
                    break
                for j in range(digits_base[i-1] if i-1 >= 0 else 0, digits_base[i]):
                    result = (result + nHr((b-1)-j+1, len(digits_base)-(i+1))) % MOD
            else:
                result = (result+1)%MOD
            return result

        return (count(int(r)) - count(int(l)-1)) % MOD


