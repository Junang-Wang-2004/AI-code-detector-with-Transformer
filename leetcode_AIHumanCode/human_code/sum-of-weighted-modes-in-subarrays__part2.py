# Time:  O(nlogn)
# Space: O(n)
import collections
import heapq


# heap, two pointers, sliding window
class Solution2(object):
    def modeWeight(self, nums, k):
        """
        """
        cnt = collections.defaultdict(int)
        max_heap = []
        result = 0
        for i in range(len(nums)):
            cnt[nums[i]] += 1
            heapq.heappush(max_heap, (-cnt[nums[i]], nums[i]))
            if i >= k-1:
                while -max_heap[0][0] != cnt[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                result += -max_heap[0][0]*max_heap[0][1]
                cnt[nums[i-k+1]] -= 1
        return result
