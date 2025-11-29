class Solution:
    def dailyTemperatures(self, temps):
        n = len(temps)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temps[stack[-1]] <= temps[i]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans
