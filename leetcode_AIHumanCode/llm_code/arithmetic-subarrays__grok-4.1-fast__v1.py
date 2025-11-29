class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check_ap(segment):
            sorted_seg = sorted(segment)
            length = len(sorted_seg)
            if length <= 1:
                return True
            step = sorted_seg[1] - sorted_seg[0]
            return all(sorted_seg[k] - sorted_seg[k - 1] == step for k in range(1, length))
        
        return [check_ap(nums[start:end + 1]) for start, end in zip(l, r)]
