class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        n = len(A)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + A[i]
        leftL = [float('-inf')] * (n + 1)
        leftM = [float('-inf')] * (n + 1)
        for i in range(1, n + 1):
            leftL[i] = leftL[i - 1]
            leftM[i] = leftM[i - 1]
            if i >= L:
                leftL[i] = max(leftL[i], presum[i] - presum[i - L])
            if i >= M:
                leftM[i] = max(leftM[i], presum[i] - presum[i - M])
        ans = float('-inf')
        for j in range(M, n + 1):
            ans = max(ans, leftL[j - M] + presum[j] - presum[j - M])
        for j in range(L, n + 1):
            ans = max(ans, leftM[j - L] + presum[j] - presum[j - L])
        return ans
