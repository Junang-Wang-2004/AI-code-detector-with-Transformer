# Time:  O(nlogn)
# Space: O(n)
import collections


# sort, freq table, difference array, line sweep
class Solution2(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        """
        cnt = collections.defaultdict(int)  # defaultdict is much faster than Counter
        for x in nums:
            cnt[x] += 1
        diff = defaultdict(int)
        for x in nums:
            diff[x] += 0
            diff[x-k] += 1
            diff[x+k+1] -= 1
        result = curr = 0
        for x, c in sorted(diff.items()):
            curr += c
            result = max(result, cnt[x]+min(curr-cnt[x], numOperations))
        return result
