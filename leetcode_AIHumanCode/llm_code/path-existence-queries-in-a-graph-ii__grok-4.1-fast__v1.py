class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        idx_sorted = sorted(range(n), key=lambda x: nums[x])
        rank_of = [0] * n
        for r, idx in enumerate(idx_sorted):
            rank_of[idx] = r
        group = [0] * n
        for i in range(1, n):
            if nums[idx_sorted[i]] - nums[idx_sorted[i - 1]] > maxDiff:
                group[i] = group[i - 1] + 1
            else:
                group[i] = group[i - 1]
        max_reach = [0] * n
        r = 0
        for l in range(n):
            while r < n and nums[idx_sorted[r]] - nums[idx_sorted[l]] <= maxDiff:
                r += 1
            max_reach[l] = r - 1
        LOG = 0
        while (1 << LOG) <= n:
            LOG += 1
        jumps = [[0] * n for _ in range(LOG)]
        for i in range(n):
            jumps[0][i] = max_reach[i]
        for k in range(1, LOG):
            for i in range(n):
                jumps[k][i] = jumps[k - 1][jumps[k - 1][i]]
        res = [-1] * len(queries)
        for qi, (a, b) in enumerate(queries):
            if a == b:
                res[qi] = 0
                continue
            ra = rank_of[a]
            rb = rank_of[b]
            if ra > rb:
                ra, rb = rb, ra
            if group[ra] != group[rb]:
                continue
            steps = 0
            pos = ra
            for k in range(LOG - 1, -1, -1):
                if jumps[k][pos] < rb:
                    pos = jumps[k][pos]
                    steps += 1 << k
            res[qi] = steps + 1
        return res
