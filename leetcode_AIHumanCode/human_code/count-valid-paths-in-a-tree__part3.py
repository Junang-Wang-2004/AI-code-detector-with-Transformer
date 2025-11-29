# Time:  O(n)
# Space: O(n)
# number theory, union find
class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.size[y] += self.size[x]
        return True

    def total(self, x):
        return self.size[self.find_set(x)]


class Solution3(object):
    def countPaths(self, n, edges):
        """
        """
        def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
            primes = []
            spf = [-1]*(n+1)  # the smallest prime factor
            for i in range(2, n+1):
                if spf[i] == -1:
                    spf[i] = i
                    primes.append(i)
                for p in primes:
                    if i*p > n or p > spf[i]:
                        break
                    spf[i*p] = p
            return spf
        
        def is_prime(u):
            return spf[u] == u

        spf = linear_sieve_of_eratosthenes(n)
        uf = UnionFind(n)
        for u, v in edges:
            u, v = u-1, v-1
            if is_prime(u+1) == is_prime(v+1) == False:
                uf.union_set(u, v) 
        result = 0
        cnt = [1]*n
        for u, v in edges:
            u, v = u-1, v-1
            if is_prime(u+1) == is_prime(v+1):
                continue
            if not is_prime(u+1):
                u, v = v, u
            result += cnt[u]*uf.total(v)
            cnt[u] += uf.total(v)
        return result
