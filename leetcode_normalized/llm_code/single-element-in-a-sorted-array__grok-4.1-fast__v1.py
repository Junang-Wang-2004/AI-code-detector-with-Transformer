class C1:

    def singleNonDuplicate(self, a1):
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            v4 = v3 ^ 1
            if v4 < len(a1) and a1[v4] == a1[v3]:
                v1 = v3 + 1
            else:
                v2 = v3
        return a1[v1]
