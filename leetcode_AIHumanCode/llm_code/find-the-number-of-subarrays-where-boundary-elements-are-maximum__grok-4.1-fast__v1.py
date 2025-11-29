class Solution:
    def numberOfSubarrays(self, nums):
        ans = 0
        stack = []
        for num in nums:
            while stack and stack[-1][0] < num:
                _, cnt = stack.pop()
                ans += cnt * (cnt + 1) // 2
            if stack and stack[-1][0] == num:
                stack[-1][1] += 1
            else:
                stack.append([num, 1])
        for _, cnt in stack:
            ans += cnt * (cnt + 1) // 2
        return ans
