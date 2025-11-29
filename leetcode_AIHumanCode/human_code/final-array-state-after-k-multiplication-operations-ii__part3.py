# Time:  O(min(nlogr, k) * logn + nlogn) = O(nlogn * logr)
# Space: O(n)
import heapq


# heap, sort, fast exponentiation
class Solution3(object):
    def getFinalState(self, nums, k, multiplier):
        """
        """
        MOD = 10**9+7
        if multiplier == 1:
            return nums
        min_heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(min_heap)
        mx = max(nums)
        for k in reversed(range(1, k+1)):
            if min_heap[0][0]*multiplier > mx:
                break
            x, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (x*multiplier, i))
        else:
            k = 0
        vals = sorted(min_heap)
        q, r = divmod(k, len(nums))
        m = pow(multiplier, q, MOD)
        result = [0]*len(nums)
        for idx, (x, i) in enumerate(vals):
            result[i] = x*m*(multiplier if idx < r else 1)%MOD
        return result
