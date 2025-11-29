from bisect import bisect_left, bisect_right

class Solution:
    def maxGCDScore(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        exponents = [0] * n
        odd_parts = [0] * n
        for i in range(n):
            val = nums[i]
            cnt = 0
            while val % 2 == 0 and val > 0:
                val //= 2
                cnt += 1
            exponents[i] = cnt
            odd_parts[i] = val
        max_e = max(exponents, default=0)
        idx_lists = [[] for _ in range(max_e + 1)]
        for i, e in enumerate(exponents):
            idx_lists[e].append(i)
        def compute_gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        current_states = {}
        best = 0
        for pos in range(n):
            o_part = odd_parts[pos]
            e_val = exponents[pos]
            next_states = {}
            key_single = (o_part, e_val)
            next_states[key_single] = [pos, pos]
            for prev_state, bounds in current_states.items():
                p_gcd, p_exp = prev_state
                ngcd = compute_gcd(p_gcd, o_part)
                nexp = min(p_exp, e_val)
                key_new = (ngcd, nexp)
                if key_new not in next_states:
                    next_states[key_new] = [float('inf'), float('inf')]
                next_states[key_new][0] = min(next_states[key_new][0], bounds[0])
                glist = idx_lists[nexp]
                lindex = bisect_left(glist, bounds[0])
                rindex = bisect_right(glist, pos) - 1
                count_low = max(0, rindex - lindex + 1)
                start_adjust = bounds[0] if count_low <= k else glist[rindex - k] + 1
                next_states[key_new][1] = min(next_states[key_new][1], start_adjust)
            current_states = next_states
            for st_key, bnds in current_states.items():
                gg, ee = st_key
                ln1 = pos - bnds[0] + 1
                sc1 = gg * ln1 * (1 << ee)
                best = max(best, sc1)
                if bnds[1] <= pos:
                    ln2 = pos - bnds[1] + 1
                    sc2 = gg * ln2 * (1 << (ee + 1))
                    best = max(best, sc2)
        return best
