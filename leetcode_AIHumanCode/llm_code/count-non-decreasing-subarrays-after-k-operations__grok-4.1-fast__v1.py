from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        answer = 0
        current_cost = 0
        monotonic = deque()
        window_right = n - 1
        for window_left in range(n - 1, -1, -1):
            while monotonic and nums[monotonic[-1]] < nums[window_left]:
                removed = monotonic.pop()
                next_seg = monotonic[-1] - 1 if monotonic else window_right
                current_cost += (next_seg - removed + 1) * (nums[window_left] - nums[removed])
            monotonic.append(window_left)
            while current_cost > k:
                current_cost -= nums[monotonic[0]] - nums[window_right]
                if monotonic[0] == window_right:
                    monotonic.popleft()
                window_right -= 1
            answer += window_right - window_left + 1
        return answer
