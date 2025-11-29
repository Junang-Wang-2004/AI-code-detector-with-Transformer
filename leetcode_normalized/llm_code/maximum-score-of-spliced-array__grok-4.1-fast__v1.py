class C1:

    def maximumsSplicedArray(self, a1, a2):
        v1 = v2 = v3 = v4 = v5 = v6 = 0
        v7 = len(a1)
        for v8 in range(v7):
            v1 += a1[v8]
            v9 = a2[v8] - a1[v8]
            v5 = max(0, v5 + v9)
            v3 = max(v3, v5)
            v2 += a2[v8]
            v10 = a1[v8] - a2[v8]
            v6 = max(0, v6 + v10)
            v4 = max(v4, v6)
        return max(v1 + v3, v2 + v4)
