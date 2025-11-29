# Time:  O(nlogn)
# Space: O(n)

import collections
import itertools
import heapq


# heap
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        """
        result = []
        cnt = collections.Counter()
        max_heap = []
        for x, f in zip(nums, freq):
            cnt[x] += f
            heapq.heappush(max_heap, (-cnt[x], x))
            while max_heap and -max_heap[0][0] != cnt[max_heap[0][1]]:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0] if max_heap else 0)
        return result


