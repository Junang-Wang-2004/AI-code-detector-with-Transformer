from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.comp_size = [1] * n

    def get_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get_root(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        rx, ry = self.get_root(x), self.get_root(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.comp_size[ry] += self.comp_size[rx]
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
            self.comp_size[rx] += self.comp_size[ry]
        else:
            self.parent[ry] = rx
            self.comp_size[rx] += self.comp_size[ry]
            self.rank[rx] += 1


class Solution:
    def largestComponentSize(self, A):
        def extract_primes(val):
            primes = []
            if val < 2:
                return primes
            while val % 2 == 0:
                primes.append(2)
                val //= 2
                break
            f = 3
            while f * f <= val:
                if val % f == 0:
                    primes.append(f)
                    while val % f == 0:
                        val //= f
                f += 2
            if val > 1:
                primes.append(val)
            return primes

        n = len(A)
        if n == 0:
            return 0
        dsu = DSU(n)
        factor_groups = defaultdict(list)
        for j, num in enumerate(A):
            for pf in extract_primes(num):
                factor_groups[pf].append(j)
        for group in factor_groups.values():
            base = group[0]
            for k in group[1:]:
                dsu.merge(base, k)
        max_comp = max(dsu.comp_size[dsu.get_root(i)] for i in range(n))
        return max_comp
