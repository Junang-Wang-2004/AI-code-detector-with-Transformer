class Solution:
    def shortestSuperstring(self, A, B):
        if A in B:
            return B
        if B in A:
            return A
        def max_prefix_overlap(p, q):
            lp, lq = len(p), len(q)
            for k in range(min(lp, lq), 0, -1):
                if p[-k:] == q[:k]:
                    return k
            return 0
        ol1 = max_prefix_overlap(A, B)
        ol2 = max_prefix_overlap(B, A)
        c1 = A + B[ol1:]
        c2 = B + A[ol2:]
        return c1 if len(c1) <= len(c2) else c2
