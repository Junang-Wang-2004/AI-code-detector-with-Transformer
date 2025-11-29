class Solution(object):
    def selfDivisiblePermutationCount(self, n):
        def compute_gcd(u, v):
            while v:
                u, v = v, u % v
            return u

        candidates = [[j for j in range(n) if compute_gcd(i + 1, j + 1) == 1] for i in range(n)]
        N = 1 << n
        counts = [0] * N
        counts[0] = 1
        for idx in range(n):
            nxt = [0] * N
            for s in range(N):
                if counts[s]:
                    for num in candidates[idx]:
                        if (s & (1 << num)) == 0:
                            nxt[s | (1 << num)] += counts[s]
            counts = nxt
        return counts[N - 1]
