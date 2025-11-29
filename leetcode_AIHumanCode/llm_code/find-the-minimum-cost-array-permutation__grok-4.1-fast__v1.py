class Solution:
    def findPermutation(self, nums):
        n = len(nums)
        if n == 0:
            return []
        N = n - 1
        SHIFT = 1 << N
        FULL = SHIFT - 1
        INF = float('inf')
        cost = [[INF] * N for _ in range(SHIFT)]
        previous = [[-1] * N for _ in range(SHIFT)]
        for end in range(N):
            msk = 1 << end
            cost[msk][end] = abs(end + 1 - nums[0])
            previous[msk][end] = -1
        for msk in range(SHIFT):
            for end in range(N):
                if (msk & (1 << end)) == 0:
                    continue
                for prv in range(N):
                    if prv == end or (msk & (1 << prv)) == 0:
                        continue
                    pmsk = msk ^ (1 << end)
                    extra = abs(end + 1 - nums[prv + 1])
                    newcost = cost[pmsk][prv] + extra
                    if newcost < cost[msk][end]:
                        cost[msk][end] = newcost
                        previous[msk][end] = prv
        best_cost = INF
        best_end = -1
        for end in range(N):
            total = cost[FULL][end] + abs(nums[end + 1] - 0)
            if total < best_cost or (total == best_cost and end < best_end):
                best_cost = total
                best_end = end
        path = []
        msk = FULL
        end = best_end
        while end != -1:
            path.append(end + 1)
            prv = previous[msk][end]
            msk ^= 1 << end
            end = prv
        path.reverse()
        return [0] + path
