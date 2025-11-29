class Solution:
    def sortEvenOdd(self, nums):
        even_elements = sorted(nums[i] for i in range(0, len(nums), 2))
        odd_elements = sorted(nums[i] for i in range(1, len(nums), 2), reverse=True)
        even_pos = 0
        odd_pos = 0
        for idx in range(len(nums)):
            if idx % 2 == 0:
                nums[idx] = even_elements[even_pos]
                even_pos += 1
            else:
                nums[idx] = odd_elements[odd_pos]
                odd_pos += 1
        return nums
