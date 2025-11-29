# Time:  O(2^n + n * r), len(sums) = 2^n
#                      , r = max(sums)-min(sums)
# Space: O(2^n + r)
import collections
from functools import reduce


# optimized from solution4 (not using dict), runtime: 968 ms
class Solution2(object):
    def recoverArray(self, n, sums):
        """
        """
        min_sum, max_sum = min(sums), max(sums)
        dp = [0]*(max_sum-min_sum+1)
        for x in sums:
            dp[x-min_sum] += 1
        sorted_sums = [x for x in range(min_sum, max_sum+1) if dp[x-min_sum]]  # Time: O(r)
        shift = 0
        result = []
        for _ in range(n):  # log(2^n) times, each time costs O(2^(n-len(result)))+O(r), Total Time: O(2^n + n * r)
            new_dp = [0]*(max_sum-min_sum+1)
            new_sorted_sums = []
            new_shift = sorted_sums[0]-sorted_sums[1] if dp[sorted_sums[0]-min_sum] == 1 else 0
            assert(new_shift <= 0)
            for x in sorted_sums:
                if not dp[x-min_sum]:
                    continue
                dp[(x-new_shift)-min_sum] -= dp[x-min_sum] if new_shift else dp[x-min_sum]//2
                new_dp[(x-new_shift)-min_sum] = dp[x-min_sum]
                new_sorted_sums.append(x-new_shift)
            dp = new_dp
            sorted_sums = new_sorted_sums
            if dp[shift-min_sum]:  # contain 0, choose this side
                result.append(new_shift)
            else:  # contain no 0, choose another side and shift 0 offset
                result.append(-new_shift)
                shift -= new_shift
        return result


