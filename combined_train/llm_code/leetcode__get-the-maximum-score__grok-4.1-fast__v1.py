class C1:

    def maxSum(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        v4, v5 = (0, 0)
        v6 = 0
        while v2 < len(a1) or v3 < len(a2):
            v7 = a1[v2] if v2 < len(a1) else float('inf')
            v8 = a2[v3] if v3 < len(a2) else float('inf')
            if v7 < v8:
                v4 += v7
                v2 += 1
            elif v8 < v7:
                v5 += v8
                v3 += 1
            else:
                v6 = (v6 + max(v4, v5) + v7) % v1
                v4 = v5 = 0
                v2 += 1
                v3 += 1
        return (v6 + max(v4, v5)) % v1
