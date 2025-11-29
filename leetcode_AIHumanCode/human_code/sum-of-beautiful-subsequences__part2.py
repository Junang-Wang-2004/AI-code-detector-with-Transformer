from functools import reduce
# Time:  precompute: O(rlogr), r = max_nums
#        runtime:    O(mx * log(mx) + nlogr * (log(nlogr) + logn)), mx = max(nums)
# Space: O(rlogr)
# number theory, bit, fenwick tree
class Solution2(object):
    def totalBeauty(self, nums):
        """
        """
        def count(arr):
            val_to_idx = {x:i for i, x in enumerate(sorted(set(arr)))}  # coordinate compression
            bit = BIT(len(val_to_idx))
            for x in arr:
                bit.add(val_to_idx[x], bit.query(val_to_idx[x]-1)+1)
            return bit.query(len(val_to_idx)-1)

        mx = max(nums)
        lookup = [[] for _ in range(mx+1)]
        for x in nums:
            for d in FACTORS[x]:
                lookup[d].append(x)
        result = 0
        cnt = [0]*(mx+1)
        for g in reversed(range(1, mx+1)):
            cnt[g] = count(lookup[g])
            for ng in range(g+g, mx+1, g):
                cnt[g] -= cnt[ng]
            result = (result+g*cnt[g])%MOD
        return result
