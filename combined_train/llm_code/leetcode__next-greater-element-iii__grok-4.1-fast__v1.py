class C1:

    def nextGreaterElement(self, a1):
        v1 = [int(c) for v2 in str(a1)]
        v3 = len(v1)
        v4 = -1
        for v5 in range(v3 - 2, -1, -1):
            if v1[v5] < v1[v5 + 1]:
                v4 = v5
                break
        if v4 == -1:
            return -1
        v6 = -1
        for v7 in range(v3 - 1, v4, -1):
            if v1[v7] > v1[v4]:
                v6 = v7
                break
        v1[v4], v1[v6] = (v1[v6], v1[v4])
        v1[v4 + 1:] = reversed(v1[v4 + 1:])
        v8 = 0
        for v9 in v1:
            v8 = v8 * 10 + v9
        return v8 if v8 <= 2147483647 else -1
