# Time:  O(n)
# Space: O(n)

import collections


# stars and bars, combinatorics
class Solution(object):
    def countOfArrays(self, n, m, k):
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

        lookup = collections.defaultdict(list)
        def pow(a, b):
            while len(lookup[a]) <= b:
                lookup[a].append((lookup[a][-1]*a)%MOD if lookup[a] else 1)
            return lookup[a][b]

        MOD = 10**9+7
        even, odd = m//2, (m+1)//2
        result = 0
        if k == 0:
            result = (result+pow(odd, n))%MOD
        for x in range(1, (n+1-k)//2+1):  # since (n-(k+x))-((x+1)-2) >= 0, so x <= (n+1-k)/2
            result = (result+(nHr(x, (k+x)-x)*nHr(x+1, (n-(k+x))-((x+1)-2))*pow(even, k+x)*pow(odd, n-(k+x))%MOD))%MOD
        return result


