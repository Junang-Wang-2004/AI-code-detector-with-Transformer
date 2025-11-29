import collections
import bisect

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = collections.Counter(nums)
        f = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            k = d
            while k <= max_val:
                f[d] += freq[k]
                k += d
        exact = [0] * (max_val + 1)
        for d in range(max_val, 0, -1):
            total_pairs_div_d = f[d] * (f[d] - 1) // 2
            subtr = 0
            mult = d * 2
            while mult <= max_val:
                subtr += exact[mult]
                mult += d
            exact[d] = total_pairs_div_d - subtr
        cum_pairs = [0]
        for d in range(1, max_val + 1):
            cum_pairs.append(cum_pairs[-1] + exact[d])
        result = []
        for q in queries:
            result.append(bisect.bisect_left(cum_pairs, q))
        return result
