import collections

class Solution:
    def continuousSubarrays(self, nums):
        min_queue = collections.deque()
        max_queue = collections.deque()
        window_left = 0
        answer = 0
        n = len(nums)
        for end in range(n):
            while min_queue and nums[min_queue[-1]] > nums[end]:
                min_queue.pop()
            min_queue.append(end)
            while max_queue and nums[max_queue[-1]] < nums[end]:
                max_queue.pop()
            max_queue.append(end)
            while window_left <= end:
                while min_queue and min_queue[0] < window_left:
                    min_queue.popleft()
                while max_queue and max_queue[0] < window_left:
                    max_queue.popleft()
                if nums[max_queue[0]] - nums[min_queue[0]] <= 2:
                    break
                window_left += 1
            answer += end - window_left + 1
        return answer
