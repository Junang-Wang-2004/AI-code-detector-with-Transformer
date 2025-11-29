class Solution:
    def getPermutationIndex(self, perm):
        MOD = 1000000007
        n = len(perm)
        facts = [1] * (n + 1)
        for i in range(1, n + 1):
            facts[i] = facts[i - 1] * i % MOD
        ft = [0] * (n + 2)

        def update(idx, delta):
            while idx <= n:
                ft[idx] = (ft[idx] + delta) % MOD
                idx += idx & -idx

        def prefix_sum(idx):
            res = 0
            while idx > 0:
                res = (res + ft[idx]) % MOD
                idx -= idx & -idx
            return res

        rank = 0
        for pos in range(n):
            num = perm[pos]
            used_below = prefix_sum(num - 1)
            avail_below = (num - 1 - used_below) % MOD
            rank = (rank + avail_below * facts[n - 1 - pos] % MOD) % MOD
            update(num, 1)
        return rank
