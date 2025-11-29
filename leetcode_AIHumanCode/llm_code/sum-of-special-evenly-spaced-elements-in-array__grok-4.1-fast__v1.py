class Solution(object):
    def solve(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        ans = []
        thresh = int(n ** 0.5) + 1
        pre = {}
        for st in range(1, thresh + 1):
            pre[st] = [[] for _ in range(st)]
            for r in range(st):
                ps = [0]
                p = r
                while p < n:
                    ps.append((ps[-1] + nums[p]) % MOD)
                    p += st
                pre[st][r] = ps
        for x, y in queries:
            if y * y > n:
                sm = 0
                i = x
                while i < n:
                    sm = (sm + nums[i]) % MOD
                    i += y
                ans.append(sm)
            else:
                r = x % y
                ps = pre[y][r]
                nt = len(ps) - 1
                k = min(x // y, nt)
                sm = (ps[-1] - ps[k] + MOD) % MOD
                ans.append(sm)
        return ans
