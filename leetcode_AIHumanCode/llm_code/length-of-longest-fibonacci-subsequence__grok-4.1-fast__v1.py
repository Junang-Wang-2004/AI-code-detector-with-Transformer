class Solution(object):
    def lenLongestFibSubseq(self, A):
        n = len(A)
        pos = {A[i]: i for i in range(n)}
        memo = {}
        longest = 2
        for j in range(n):
            for i in range(j):
                prev = A[j] - A[i]
                if prev in pos:
                    k = pos[prev]
                    if k < i:
                        prev_length = memo.get((k, i), 2)
                        curr_length = prev_length + 1
                        memo[(i, j)] = curr_length
                        if curr_length > longest:
                            longest = curr_length
        return longest if longest > 2 else 0
