class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        i1 = i2 = -1
        for k in range(len(A)):
            if A[k] != B[k]:
                if i1 < 0:
                    i1 = k
                elif i2 < 0:
                    i2 = k
                else:
                    return False
        if i1 < 0:
            seen = set()
            for c in A:
                if c in seen:
                    return True
                seen.add(c)
            return False
        if i2 < 0:
            return False
        return A[i1] == B[i2] and A[i2] == B[i1]
