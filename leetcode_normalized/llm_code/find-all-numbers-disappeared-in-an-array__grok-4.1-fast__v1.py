class C1:

    def findDisappearedNumbers(self, a1):
        v1 = len(a1)
        v2 = 0
        while v2 < v1:
            v3 = a1[v2] - 1
            if 1 <= a1[v2] <= v1 and a1[v3] != a1[v2]:
                a1[v3], a1[v2] = (a1[v2], a1[v3])
            else:
                v2 += 1
        return [j + 1 for v4 in range(v1) if a1[v4] != v4 + 1]
