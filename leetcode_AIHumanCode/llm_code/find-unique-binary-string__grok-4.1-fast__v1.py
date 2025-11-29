class Solution:
    def findDifferentBinaryString(self, nums):
        size = len(nums)
        output = []
        for idx in range(size):
            bit = nums[idx][idx]
            output.append('1' if bit == '0' else '0')
        return ''.join(output)
