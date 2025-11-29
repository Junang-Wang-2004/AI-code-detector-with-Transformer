import heapq

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums)
        m = n // 3
        min_sums_left = [0] * (m + 1)
        pq_left = []
        cur_min_sum = 0
        for i in range(m):
            val = nums[i]
            heapq.heappush(pq_left, -val)
            cur_min_sum += val
        min_sums_left[0] = cur_min_sum
        for j in range(1, m + 1):
            val = nums[m + j - 1]
            popped_neg = heapq.heappushpop(pq_left, -val)
            popped_val = -popped_neg
            cur_min_sum += val - popped_val
            min_sums_left[j] = cur_min_sum

        max_sums_right = [0] * (m + 1)
        pq_right = []
        cur_max_sum = 0
        for i in range(n - m, n):
            val = nums[i]
            heapq.heappush(pq_right, val)
            cur_max_sum += val
        max_sums_right[0] = cur_max_sum
        for j in range(1, m + 1):
            val = nums[2 * m - j]
            popped = heapq.heappushpop(pq_right, val)
            cur_max_sum += val - popped
            max_sums_right[j] = cur_max_sum

        ans = float('inf')
        for i in range(m + 1):
            ans = min(ans, min_sums_left[i] - max_sums_right[m - i])
        return ans
