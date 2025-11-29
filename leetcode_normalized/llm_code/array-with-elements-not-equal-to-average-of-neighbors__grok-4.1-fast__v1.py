class C1:

    def rearrangeArray(self, a1):
        a1.sort()
        v1 = len(a1)
        v2 = (v1 + 1) // 2
        v3 = v1 // 2
        v4 = [a1[v2 - 1 - p] for v5 in range(v2)]
        v6 = [a1[v1 - 1 - q] for v7 in range(v3)]
        v8, v9 = (0, 0)
        for v10 in range(v1):
            if v10 % 2 == 0:
                a1[v10] = v4[v8]
                v8 += 1
            else:
                a1[v10] = v6[v9]
                v9 += 1
        return a1
