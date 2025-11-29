import heapq

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)
        if n == 0 or k == 0:
            return 0
        LOG = [0] * (n + 2)
        for i in range(2, n + 1):
            LOG[i] = LOG[i // 2] + 1
        st_min = [[0] * n for _ in range(LOG[n] + 1)]
        st_max = [[0] * n for _ in range(LOG[n] + 1)]
        for i in range(n):
            st_min[0][i] = nums[i]
            st_max[0][i] = nums[i]
        for j in range(1, LOG[n] + 1):
            for i in range(n - (1 << j) + 1):
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + (1 << (j - 1))])
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + (1 << (j - 1))])
        def range_min(L, R):
            lg = LOG[R - L + 1]
            return min(st_min[lg][L], st_min[lg][R - (1 << lg) + 1])
        def range_max(L, R):
            lg = LOG[R - L + 1]
            return max(st_max[lg][L], st_max[lg][R - (1 << lg) + 1])
        heap = [(-(range_max(i, n - 1) - range_min(i, n - 1)), i, n - 1) for i in range(n)]
        heapq.heapify(heap)
        total = 0
        operations = 0
        while operations < k and heap:
            _, left_end, right_end = heapq.heappop(heap)
            total += range_max(left_end, right_end) - range_min(left_end, right_end)
            operations += 1
            if left_end < right_end:
                new_val = -(range_max(left_end, right_end - 1) - range_min(left_end, right_end - 1))
                heapq.heappush(heap, (new_val, left_end, right_end - 1))
        return total
