class C1:

    def firstMissingPositive(self, a1):
        v1 = len(a1)
        v2 = 0
        while v2 < v1:
            v3 = a1[v2] - 1
            if 0 <= v3 < v1 and a1[v3] != a1[v2]:
                a1[v2], a1[v3] = (a1[v3], a1[v2])
            else:
                v2 += 1
        v2 = 0
        while v2 < v1 and a1[v2] == v2 + 1:
            v2 += 1
        return v2 + 1
