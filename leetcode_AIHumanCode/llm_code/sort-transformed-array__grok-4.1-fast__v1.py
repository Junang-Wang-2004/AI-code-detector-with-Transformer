class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        n = len(nums)
        if n == 0:
            return []
        def compute(x):
            return a * x * x + b * x + c
        output = [0] * n
        i, j = 0, n - 1
        if a > 0:
            k = n - 1
            while i <= j:
                left_val = compute(nums[i])
                right_val = compute(nums[j])
                if left_val > right_val:
                    output[k] = left_val
                    i += 1
                else:
                    output[k] = right_val
                    j -= 1
                k -= 1
        else:
            k = 0
            while i <= j:
                left_val = compute(nums[i])
                right_val = compute(nums[j])
                if left_val < right_val:
                    output[k] = left_val
                    i += 1
                else:
                    output[k] = right_val
                    j -= 1
                k += 1
        return output
