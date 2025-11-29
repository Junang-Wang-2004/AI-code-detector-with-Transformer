class C1:

    def findMedianSortedArrays(self, a1, a2):
        if len(a1) > len(a2):
            a1, a2 = (a2, a1)
        v3, v4 = (len(a1), len(a2))
        v5 = v3 + v4
        v6 = (v5 + 1) // 2
        v7, v8 = (0, v3)
        while v7 <= v8:
            v9 = (v7 + v8) // 2
            v10 = v6 - v9
            v11 = a1[v9 - 1] if v9 > 0 else float('-inf')
            v12 = a2[v10 - 1] if v10 > 0 else float('-inf')
            v13 = a1[v9] if v9 < v3 else float('inf')
            v14 = a2[v10] if v10 < v4 else float('inf')
            if v11 > v14:
                v8 = v9 - 1
            elif v12 > v13:
                v7 = v9 + 1
            else:
                if v5 % 2 == 1:
                    return max(v11, v12)
                return (max(v11, v12) + min(v13, v14)) / 2
