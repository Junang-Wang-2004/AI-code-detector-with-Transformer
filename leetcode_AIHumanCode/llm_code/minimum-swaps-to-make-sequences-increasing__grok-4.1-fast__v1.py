class Solution(object):
    def minSwap(self, A, B):
        prev_noswap = 0
        prev_swap = 1
        for i in range(1, len(A)):
            curr_noswap = float('inf')
            curr_swap = float('inf')
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                curr_noswap = min(curr_noswap, prev_noswap)
                curr_swap = min(curr_swap, prev_swap + 1)
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                curr_noswap = min(curr_noswap, prev_swap)
                curr_swap = min(curr_swap, prev_noswap + 1)
            prev_noswap = curr_noswap
            prev_swap = curr_swap
        return min(prev_noswap, prev_swap)
