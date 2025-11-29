# Time:  O(r * (n + q)), r is the max of nums
# Space: O(r * n)

class Solution(object):
    def minDifference(self, nums, queries):
        """
        """
        INF = float("inf")
        prefix = [[0]*(max(nums)+1)]
        for num in nums:
            prefix.append(prefix[-1][:])
            prefix[-1][num] += 1
        result = []
        for l, r in queries:
            min_diff, prev = INF, -1
            for num in range(len(prefix[0])):
                if not (prefix[l][num] < prefix[r+1][num]):
                    continue
                if prev != -1:
                    min_diff = min(min_diff, num-prev)
                prev = num
            result.append(min_diff if min_diff != INF else -1)
        return result


