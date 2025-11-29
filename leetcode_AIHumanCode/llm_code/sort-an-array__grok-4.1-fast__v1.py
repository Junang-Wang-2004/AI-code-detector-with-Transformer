class Solution:
    def sortArray(self, nums):
        def push_down(pos, limit):
            nxt = 2 * pos + 1
            while nxt <= limit:
                if nxt + 1 <= limit and nums[nxt + 1] > nums[nxt]:
                    nxt += 1
                if nums[pos] < nums[nxt]:
                    nums[pos], nums[nxt] = nums[nxt], nums[pos]
                    pos = nxt
                    nxt = 2 * pos + 1
                else:
                    break

        size = len(nums)
        for idx in range(size // 2 - 1, -1, -1):
            push_down(idx, size - 1)
        for idx in range(size - 1, 0, -1):
            nums[0], nums[idx] = nums[idx], nums[0]
            push_down(0, idx - 1)
        return nums
