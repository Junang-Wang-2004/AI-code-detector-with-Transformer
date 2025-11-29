# Time:  O(n * 2^n), len(sums) = 2^n
# Space: O(2^n)
import collections


# optimized from solution4 (not using OrderedDict), runtime: 1024 ms
class Solution4(object):
    def recoverArray(self, n, sums):
        """
        """
        dp = {k: v for k, v in collections.Counter(sums).items()}
        sorted_sums = sorted(dp.keys())  # Time: O(2^n * log(2^n)) = O(n * 2^n)
        shift = 0
        result = []
        for _ in range(n):  # log(2^n) times, each time costs O(2^(n-len(result))), Total Time: O(2^n)
            new_dp = {}
            new_sorted_sums = []
            new_shift = sorted_sums[0]-sorted_sums[1] if dp[sorted_sums[0]] == 1 else 0
            assert(new_shift <= 0)
            for x in sorted_sums:
                if not dp[x]:
                    continue
                dp[x-new_shift] -= dp[x] if new_shift else dp[x]//2
                new_dp[x-new_shift] = dp[x]
                new_sorted_sums.append(x-new_shift)
            dp = new_dp
            sorted_sums = new_sorted_sums
            if shift in dp:  # contain 0, choose this side
                result.append(new_shift)
            else:  # contain no 0, choose another side and shift 0 offset
                result.append(-new_shift)
                shift -= new_shift
        return result


