class Solution:
    def advantageCount(self, A, B):
        n = len(A)
        result = [0] * n
        a_sorted = sorted(A)
        b_pos = sorted(range(n), key=lambda x: B[x])
        i = 0
        extras = []
        for pos in b_pos:
            val = B[pos]
            while i < n and a_sorted[i] <= val:
                extras.append(a_sorted[i])
                i += 1
            if i < n:
                result[pos] = a_sorted[i]
                i += 1
        ptr = 0
        for j in range(n):
            if result[j] == 0:
                result[j] = extras[ptr]
                ptr += 1
        return result
