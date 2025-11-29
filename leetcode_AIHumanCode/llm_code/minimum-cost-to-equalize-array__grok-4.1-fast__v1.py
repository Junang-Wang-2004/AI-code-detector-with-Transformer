class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        mod = 10**9 + 7
        n = len(nums)
        mx_val = max(nums)
        sm = sum(nums)
        init_need = mx_val * n - sm
        if n <= 2 or cost1 * 2 <= cost2:
            return (init_need * cost1) % mod
        mn_val = min(nums)
        max_gap = mx_val - mn_val
        init_forced = max(0, 2 * max_gap - init_need)
        def get_cost(total_need, forced):
            extra_pairs = total_need - forced
            ones = forced + (extra_pairs % 2)
            twos = extra_pairs // 2
            return ones * cost1 + twos * cost2
        ans = get_cost(init_need, init_forced)
        divider = n - 2
        raise_amount, leftover_forced = divmod(init_forced, divider)
        raised_need = init_need + n * raise_amount
        ans = min(ans, get_cost(raised_need, leftover_forced))
        raised_need += n
        ans = min(ans, (raised_need % 2) * cost1 + (raised_need // 2) * cost2)
        raised_need += n
        ans = min(ans, (raised_need % 2) * cost1 + (raised_need // 2) * cost2)
        return ans % mod
