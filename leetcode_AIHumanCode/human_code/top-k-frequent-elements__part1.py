# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for i, count in counts.items():
            buckets[count].append(i)

        result = []
        for i in reversed(range(len(buckets))):
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
        return result


