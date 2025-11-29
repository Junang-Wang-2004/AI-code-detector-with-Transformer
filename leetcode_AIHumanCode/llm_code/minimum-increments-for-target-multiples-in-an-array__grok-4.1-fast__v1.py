class Solution:
    def minimumIncrements(self, nums, target):
        INF = float('inf')

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x // gcd(x, y) * y

        m = len(target)
        states = 1 << m
        subset_lcms = [0] * states
        for s in range(states):
            val = 1
            for j in range(m):
                if s & (1 << j):
                    val = lcm(val, target[j])
            subset_lcms[s] = val

        costs = [INF] * states
        costs[0] = 0

        for val in nums:
            next_costs = costs[:]
            for s in range(states):
                if costs[s] == INF:
                    continue
                avail = (states - 1) ^ s
                t = avail
                while t:
                    clcm = subset_lcms[t]
                    rem = val % clcm
                    extra = 0 if rem == 0 else clcm - rem
                    ns = s | t
                    next_costs[ns] = min(next_costs[ns], costs[s] + extra)
                    t = (t - 1) & avail
            costs = next_costs

        return costs[states - 1]
