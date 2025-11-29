# Time:  O(n * 2^n), len(sums) = 2^n
# Space: O(2^n)
import collections


# runtime: 1720 ms
class Solution5(object):
    def recoverArray(self, n, sums):
        """
        """
        dp = OrderedDict(sorted(collections.Counter(sums).items()))  # Time: O(2^n * log(2^n)) = O(n * 2^n)
        shift = 0
        result = []
        for _ in range(n):  # log(2^n) times, each time costs O(2^(n-len(result))), Total Time: O(2^n)
            new_dp = OrderedDict()
            it = iter(dp)
            min_sum = next(it)
            new_shift = min_sum-next(it) if dp[min_sum] == 1 else 0
            assert(new_shift <= 0)
            for x in dp.keys():
                if not dp[x]:
                    continue
                dp[x-new_shift] -= dp[x] if new_shift else dp[x]//2
                new_dp[x-new_shift] = dp[x]
            dp = new_dp
            if shift in dp:  # contain 0, choose this side
                result.append(new_shift)
            else:  # contain no 0, choose another side and shift 0 offset
                result.append(-new_shift)
                shift -= new_shift
        return result
