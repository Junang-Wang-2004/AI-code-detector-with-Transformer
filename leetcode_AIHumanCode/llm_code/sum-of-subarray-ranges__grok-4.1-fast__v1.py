class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)
        total = 0
        
        # Compute sum of maximums
        left_bound = [-1] * n
        monotonic = []
        for i in range(n):
            while monotonic and nums[monotonic[-1]] <= nums[i]:
                monotonic.pop()
            if monotonic:
                left_bound[i] = monotonic[-1]
            monotonic.append(i)
        
        right_bound = [n] * n
        monotonic = []
        for i in range(n - 1, -1, -1):
            while monotonic and nums[monotonic[-1]] < nums[i]:
                monotonic.pop()
            if monotonic:
                right_bound[i] = monotonic[-1]
            monotonic.append(i)
        
        for i in range(n):
            l_span = i - left_bound[i]
            r_span = right_bound[i] - i
            total += nums[i] * l_span * r_span
        
        # Compute sum of minimums
        left_bound = [-1] * n
        monotonic = []
        for i in range(n):
            while monotonic and nums[monotonic[-1]] >= nums[i]:
                monotonic.pop()
            if monotonic:
                left_bound[i] = monotonic[-1]
            monotonic.append(i)
        
        right_bound = [n] * n
        monotonic = []
        for i in range(n - 1, -1, -1):
            while monotonic and nums[monotonic[-1]] > nums[i]:
                monotonic.pop()
            if monotonic:
                right_bound[i] = monotonic[-1]
            monotonic.append(i)
        
        for i in range(n):
            l_span = i - left_bound[i]
            r_span = right_bound[i] - i
            total -= nums[i] * l_span * r_span
        
        return total
