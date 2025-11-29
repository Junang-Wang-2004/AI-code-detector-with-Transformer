class Solution:
    def minOperations(self, nums):
        def search_insert(tails, target):
            left = 0
            right = len(tails)
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        tails = []
        for val in nums:
            pos = search_insert(tails, -val)
            if pos == len(tails):
                tails.append(-val)
            else:
                tails[pos] = -val
        return len(tails)
