class C1:

    def restoreString(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3, v4 in enumerate(a2):
            v2[v4] = v3
        v5 = []
        for v6 in range(v1):
            v5.append(a1[v2[v6]])
        return ''.join(v5)
