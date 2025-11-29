import collections

class Solution:
    def minimumValueSum(self, nums, and_values):
        n = len(nums)
        m = len(and_values)
        if n < m:
            return -1
        INF = 10**20
        dp = [INF] * (n + 1)
        dp[0] = 0
        BITS = max(nums).bit_length() if nums else 0
        BITS = max(BITS, 1)
        for j in range(m):
            target = and_values[j]
            new_dp = [INF] * (n + 1)
            bit_cnt = [0] * BITS
            lft = j
            qidx = j
            trail = [0] * (n + 1)
            deq = collections.deque()
            for rgt in range(j, n):
                for b in range(BITS):
                    if nums[rgt] & (1 << b):
                        bit_cnt[b] += 1
                wsize = rgt - lft + 1
                crnt_and = 0
                for b in range(BITS):
                    if bit_cnt[b] == wsize:
                        crnt_and |= (1 << b)
                if crnt_and <= target:
                    while lft <= rgt:
                        twsize = rgt - lft + 1
                        tand = 0
                        for b in range(BITS):
                            if bit_cnt[b] == twsize:
                                tand |= (1 << b)
                        if tand > target:
                            break
                        for b in range(BITS):
                            if nums[lft] & (1 << b):
                                bit_cnt[b] -= 1
                        lft += 1
                    lft -= 1
                    for b in range(BITS):
                        if nums[lft] & (1 << b):
                            bit_cnt[b] += 1
                wsize = rgt - lft + 1
                crnt_and = 0
                for b in range(BITS):
                    if bit_cnt[b] == wsize:
                        crnt_and |= (1 << b)
                superset = (target & nums[rgt]) == target
                if superset:
                    trail[rgt + 1] = trail[rgt] + 1
                else:
                    trail[rgt + 1] = 0
                if crnt_and == target:
                    while qidx <= lft:
                        while deq and dp[deq[-1]] >= dp[qidx]:
                            deq.pop()
                        deq.append(qidx)
                        qidx += 1
                    mn_start = max(j, lft - trail[lft])
                    while deq and deq[0] < mn_start:
                        deq.popleft()
                    if deq:
                        new_dp[rgt + 1] = min(new_dp[rgt + 1], dp[deq[0]] + nums[rgt])
            dp = new_dp
        return dp[n] if dp[n] < INF else -1
