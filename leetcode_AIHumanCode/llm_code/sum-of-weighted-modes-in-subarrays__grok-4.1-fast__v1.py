import collections
import heapq

class Solution:
    def modeWeight(self, nums, k):
        frequency = collections.Counter()
        priority_queue = []
        total = 0
        j = 0
        for i in range(len(nums)):
            current = nums[i]
            frequency[current] += 1
            heapq.heappush(priority_queue, (-frequency[current], current))
            while i - j + 1 > k:
                leaving = nums[j]
                frequency[leaving] -= 1
                j += 1
            if i - j + 1 == k:
                while priority_queue and frequency[priority_queue[0][1]] != -priority_queue[0][0]:
                    heapq.heappop(priority_queue)
                max_count = -priority_queue[0][0]
                mode_value = priority_queue[0][1]
                total += max_count * mode_value
        return total
