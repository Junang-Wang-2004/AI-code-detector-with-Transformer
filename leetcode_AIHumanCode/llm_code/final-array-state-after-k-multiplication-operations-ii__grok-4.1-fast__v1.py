import math

class Solution:
    def getFinalState(self, nums, k, multiplier):
        MOD = 10**9 + 7
        if multiplier == 1:
            return nums
        n = len(nums)
        log_mult = math.log(multiplier)
        exponents = [math.log(x) / log_mult for x in nums]
        max_exp = max(exponents)
        sorted_exps = sorted((e, idx) for idx, e in enumerate(exponents))
        def mult_count(e_val, tgt):
            return int(tgt - e_val + 1e-10)
        def feasible(tgt_val):
            accum = 0
            for e_val, _ in sorted_exps:
                cnt = mult_count(e_val, tgt_val)
                if cnt <= 0:
                    break
                accum += cnt
                if accum > k:
                    return False
            return accum <= k
        lo = 0
        hi = int(max_exp) + 2
        while lo < hi:
            md = (lo + hi + 1) // 2
            if feasible(md):
                lo = md
            else:
                hi = md - 1
        max_tgt = lo
        counts = [0] * n
        consumed = 0
        for e_val, idx in sorted_exps:
            cnt = mult_count(e_val, max_tgt)
            if cnt <= 0:
                break
            counts[idx] = cnt
            consumed += cnt
        leftover = k - consumed
        full_rounds, extras = divmod(leftover, n)
        pow_full = pow(multiplier, full_rounds, MOD)
        curr_exponents = [exponents[i] + counts[i] for i in range(n)]
        sorted_indices = list(range(n))
        sorted_indices.sort(key=lambda x: curr_exponents[x])
        prefixed = [(nums[i] * pow(multiplier, counts[i], MOD)) % MOD for i in range(n)]
        ans = [0] * n
        for position, idx in enumerate(sorted_indices):
            addl = multiplier if position < extras else 1
            ans[idx] = prefixed[idx] * pow_full * addl % MOD
        return ans
