class Solution:
    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n <= 1:
            return True
        max_val = max(nums)
        small_primes = self._generate_primes(int(max_val ** 0.5) + 1)

        def extract_primes(num):
            unique_primes = set()
            v = num
            for p in small_primes:
                if p * p > v:
                    break
                if v % p == 0:
                    unique_primes.add(p)
                    while v % p == 0:
                        v //= p
            if v > 1:
                unique_primes.add(v)
            return unique_primes

        def find_root(x, par):
            if par[x] != x:
                par[x] = find_root(par[x], par)
            return par[x]

        def merge_sets(a, b, par, rnk):
            ra = find_root(a, par)
            rb = find_root(b, par)
            if ra == rb:
                return
            if rnk[ra] < rnk[rb]:
                par[ra] = rb
            elif rnk[ra] > rnk[rb]:
                par[rb] = ra
            else:
                par[rb] = ra
                rnk[ra] += 1

        par = list(range(n))
        rnk = [0] * n
        prime_holder = {}
        for i, value in enumerate(nums):
            if value <= 1:
                continue
            primes_set = extract_primes(value)
            for prime in primes_set:
                if prime in prime_holder:
                    merge_sets(i, prime_holder[prime], par, rnk)
                prime_holder[prime] = i

        start_root = find_root(0, par)
        for j in range(1, n):
            if find_root(j, par) != start_root:
                return False
        return True

    def _generate_primes(self, limit):
        if limit < 2:
            return []
        flags = [True] * (limit + 1)
        flags[0] = flags[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if flags[i]:
                for multiple in range(i * i, limit + 1, i):
                    flags[multiple] = False
        return [idx for idx in range(2, limit + 1) if flags[idx]]
