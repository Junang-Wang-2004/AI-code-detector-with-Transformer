class C1:

    def minSwaps(self, a1):
        v1 = len(a1)
        v2 = []
        for v3 in a1:
            v4 = 0
            while v4 < v1 and v3[v1 - 1 - v4] == 0:
                v4 += 1
            v2.append(v4)
        v5 = 0
        for v6 in range(v1 - 1):
            v7 = v1 - 1 - v6
            v8 = next((i for v9 in range(v6, v1) if v2[v9] >= v7), -1)
            if v8 == -1:
                return -1
            v5 += v8 - v6
            v10 = v2.pop(v8)
            v2.insert(v6, v10)
        return v5
