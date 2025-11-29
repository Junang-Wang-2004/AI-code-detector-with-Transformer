class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        cons = {}
        mx = 0
        for p, v in requirements:
            cons[p] = v
            if v > mx:
                mx = v
        curr_ways = [0] * (mx + 1)
        curr_ways[0] = 1
        for idx in range(n):
            next_ways = [0] * (mx + 1)
            wsize = idx + 1
            accum = 0
            for s in range(mx + 1):
                accum = (accum + curr_ways[s]) % MOD
                drop_idx = s - wsize
                if drop_idx >= 0:
                    accum = (accum - curr_ways[drop_idx] + MOD) % MOD
                if idx not in cons or s == cons[idx]:
                    next_ways[s] = accum
            curr_ways = next_ways
        return curr_ways[mx]
