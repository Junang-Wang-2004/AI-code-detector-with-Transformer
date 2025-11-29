class Solution:
    def numberWays(self, hats):
        MOD = 10**9 + 7
        MAX_HAT = 40
        n = len(hats)
        can_wear = [[] for _ in range(MAX_HAT)]
        for idx in range(n):
            for hat_id in hats[idx]:
                can_wear[hat_id - 1].append(idx)
        ways = [0] * (1 << n)
        ways[0] = 1
        for h in range(MAX_HAT):
            wearers = can_wear[h]
            if not wearers:
                continue
            fresh_ways = ways[:]
            for subset in range(1 << n):
                if ways[subset] == 0:
                    continue
                for wearer in wearers:
                    if (subset & (1 << wearer)) == 0:
                        new_subset = subset | (1 << wearer)
                        fresh_ways[new_subset] = (fresh_ways[new_subset] + ways[subset]) % MOD
            ways = fresh_ways
        return ways[(1 << n) - 1]
