class C1:

    def minOperations(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1 - 2):
            if a1[v3] == 0:
                a1[v3 + 1] = 1 - a1[v3 + 1]
                a1[v3 + 2] = 1 - a1[v3 + 2]
                v2 += 1
        if a1[v1 - 2] == 1 and a1[v1 - 1] == 1:
            return v2
        return -1
