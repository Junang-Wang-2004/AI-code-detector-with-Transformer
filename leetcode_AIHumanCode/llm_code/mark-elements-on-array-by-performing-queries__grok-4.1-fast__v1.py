class Solution:
    def unmarkedSumArray(self, nums, queries):
        n = len(nums)
        current_sum = 0
        for val in nums:
            current_sum += val
        marked = [False] * n
        min_pq = []
        for idx in range(n):
            heapq.heappush(min_pq, (nums[idx], idx))
        ans = []
        for query_idx, count in queries:
            if not marked[query_idx]:
                marked[query_idx] = True
                current_sum -= nums[query_idx]
            marked_count = 0
            while marked_count < count and min_pq:
                v, i = heapq.heappop(min_pq)
                if marked[i]:
                    continue
                marked[i] = True
                current_sum -= v
                marked_count += 1
            ans.append(current_sum)
        return ans
