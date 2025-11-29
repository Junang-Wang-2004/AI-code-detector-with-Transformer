class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        n = len(maxHeights)
        lsum = [0] * n
        stack = [-1]
        presum = 0
        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] >= maxHeights[i]:
                j = stack.pop()
                presum -= maxHeights[j] * (j - stack[-1])
            segwidth = i - stack[-1]
            presum += maxHeights[i] * segwidth
            stack.append(i)
            lsum[i] = presum
        rsum = [0] * n
        stack = [n]
        postsumm = 0
        for k in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] >= maxHeights[k]:
                j = stack.pop()
                postsumm -= maxHeights[j] * (stack[-1] - j)
            segwidth = stack[-1] - k
            postsumm += maxHeights[k] * segwidth
            stack.append(k)
            rsum[k] = postsumm
        max_total = 0
        for i in range(n):
            max_total = max(max_total, lsum[i] + rsum[i] - maxHeights[i])
        return max_total
