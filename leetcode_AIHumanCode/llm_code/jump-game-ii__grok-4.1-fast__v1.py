class Solution:
    def jump(self, A):
        n = len(A)
        farthest = 0
        current_end = 0
        jumps = 0
        i = 0
        while farthest < n - 1:
            if i > farthest:
                return -1
            while i <= current_end and i < n:
                farthest = max(farthest, i + A[i])
                i += 1
            current_end = farthest
            jumps += 1
        return jumps
