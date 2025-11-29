class Solution:
    def maxWidthRamp(self, A):
        n = len(A)
        decreasing = []
        for idx in range(n):
            if not decreasing or A[decreasing[-1]] > A[idx]:
                decreasing.append(idx)
        maximum = 0
        for pos in range(n - 1, -1, -1):
            while decreasing and A[decreasing[-1]] <= A[pos]:
                maximum = max(maximum, pos - decreasing.pop())
        return maximum
