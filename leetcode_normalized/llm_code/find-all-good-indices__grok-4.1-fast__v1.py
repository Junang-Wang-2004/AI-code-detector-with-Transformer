class C1(object):

    def goodIndices(self, a1, a2):
        v1 = len(a1)
        v2 = [1] * v1
        for v3 in range(1, v1):
            if a1[v3] <= a1[v3 - 1]:
                v2[v3] = v2[v3 - 1] + 1
        v4 = [1] * v1
        for v3 in range(v1 - 2, -1, -1):
            if a1[v3] <= a1[v3 + 1]:
                v4[v3] = v4[v3 + 1] + 1
        v5 = []
        for v6 in range(a2, v1 - a2):
            if v2[v6 - 1] >= a2 and v4[v6 + 1] >= a2:
                v5.append(v6)
        return v5
