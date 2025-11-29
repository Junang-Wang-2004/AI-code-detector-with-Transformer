from collections import deque

class Solution:
    def minCost(self, nums, x):
        n = len(nums)
        def get_cost(kk):
            wsz = kk + 1
            tot = x * kk
            q = deque()
            for ii in range(n + wsz - 1):
                ci = ii % n
                if q and ii - q[0] == wsz:
                    q.popleft()
                while q and nums[q[-1] % n] >= nums[ci]:
                    q.pop()
                q.append(ii)
                if ii >= wsz - 1:
                    tot += nums[q[0] % n]
            return tot
        lft = 0
        rgt = n
        while rgt - lft > 2:
            md1 = lft + (rgt - lft) // 3
            md2 = rgt - (rgt - lft) // 3
            if get_cost(md1) <= get_cost(md2):
                rgt = md2
            else:
                lft = md1
        res = float('inf')
        for val in range(lft, rgt + 1):
            res = min(res, get_cost(val))
        return res
