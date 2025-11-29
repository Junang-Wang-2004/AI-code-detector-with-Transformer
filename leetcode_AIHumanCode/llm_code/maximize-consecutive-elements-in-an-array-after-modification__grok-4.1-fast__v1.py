class Solution:
    def maxSelectedElements(self, nums):
        if not nums:
            return 0
        nums.sort()
        max_length = 1
        cover_end = 1
        cover_next = 1
        last = nums[0]
        for k in range(1, len(nums)):
            current = nums[k]
            delta = current - last
            if delta == 0:
                cover_next = max(cover_next, cover_end + 1)
            elif delta == 1:
                cover_end += 1
                cover_next += 1
            elif delta == 2:
                cover_end = cover_next + 1
                cover_next = 1
            else:
                cover_end = 1
                cover_next = 1
            max_length = max(max_length, cover_end, cover_next)
            last = current
        return max_length
