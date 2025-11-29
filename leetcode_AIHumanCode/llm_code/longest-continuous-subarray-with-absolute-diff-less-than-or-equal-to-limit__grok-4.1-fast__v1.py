from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_queue = deque()
        min_queue = deque()
        longest = 0
        begin = 0
        for finish in range(len(nums)):
            while max_queue and nums[max_queue[-1]] <= nums[finish]:
                max_queue.pop()
            max_queue.append(finish)
            while min_queue and nums[min_queue[-1]] >= nums[finish]:
                min_queue.pop()
            min_queue.append(finish)
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == begin:
                    max_queue.popleft()
                if min_queue[0] == begin:
                    min_queue.popleft()
                begin += 1
            longest = max(longest, finish - begin + 1)
        return longest
