import heapq


class Solution:
    def smallestRange(self, nums):
        if not nums:
            return []
        pq = []
        mx = float('-inf')
        for i, arr in enumerate(nums):
            heapq.heappush(pq, (arr[0], i, 0))
            mx = max(mx, arr[0])
        mn_rng = float('inf')
        res = (0, 0)
        mn = pq[0][0]
        if mx - mn < mn_rng:
            mn_rng = mx - mn
            res = (mn, mx)
        while pq:
            val, lst_idx, idx = heapq.heappop(pq)
            if idx + 1 == len(nums[lst_idx]):
                break
            nxt_val = nums[lst_idx][idx + 1]
            heapq.heappush(pq, (nxt_val, lst_idx, idx + 1))
            mx = max(mx, nxt_val)
            mn = pq[0][0]
            rng = mx - mn
            if rng < mn_rng:
                mn_rng = rng
                res = (mn, mx)
        return res
