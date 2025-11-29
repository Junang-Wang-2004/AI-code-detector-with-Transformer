class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        
        prev_smaller = [-1] * n
        stk = []
        for i in range(n):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                prev_smaller[i] = stk[-1]
            stk.append(i)
        
        next_smaller_or_eq = [n] * n
        stk = []
        for i in range(n):
            while stk and nums[stk[-1]] >= nums[i]:
                next_smaller_or_eq[stk.pop()] = i
            stk.append(i)
        
        maximum = 0
        for i in range(n):
            l = prev_smaller[i]
            r = next_smaller_or_eq[i]
            subarray_sum = pref[r] - pref[l + 1]
            candidate = nums[i] * subarray_sum
            if candidate > maximum:
                maximum = candidate
        return maximum % MOD
