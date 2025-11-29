class C1:

    def pancakeSort(self, a1):
        v1 = []
        v2 = len(a1)
        for v3 in range(v2, 1, -1):
            v4 = a1[:v3].index(v3)
            if v4 != v3 - 1:
                a1[:v4 + 1] = a1[:v4 + 1][::-1]
                v1.append(v4 + 1)
                a1[:v3] = a1[:v3][::-1]
                v1.append(v3)
        return v1
