import heapq

class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        n = len(nums)
        m = len(changeIndices)
        last_occurrence = [-1] * n
        for pos in range(m - 1, -1, -1):
            idx = changeIndices[pos] - 1
            if nums[idx] and last_occurrence[idx] == -1:
                last_occurrence[idx] = pos
        overall_cost = sum(nums) + n
        min_time = sum(nums[i] if last_occurrence[i] == -1 else 1 for i in range(n)) + n
        def feasible(end_time):
            priority_queue = []
            extra_slots = 0
            for step in range(end_time - 1, -1, -1):
                curr_idx = changeIndices[step] - 1
                if last_occurrence[curr_idx] != step:
                    extra_slots += 1
                    continue
                heapq.heappush(priority_queue, nums[curr_idx])
                if extra_slots:
                    extra_slots -= 1
                else:
                    extra_slots += 1
                    if priority_queue:
                        heapq.heappop(priority_queue)
            handled = sum(priority_queue) + len(priority_queue)
            return overall_cost - handled <= extra_slots
        l, r = min_time, m
        while l < r:
            half = l + (r - l) // 2
            if feasible(half):
                r = half
            else:
                l = half + 1
        return l if l <= m and feasible(l) else -1
