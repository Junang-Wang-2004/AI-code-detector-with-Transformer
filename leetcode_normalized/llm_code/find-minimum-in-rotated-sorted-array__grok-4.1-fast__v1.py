class C1:

    def findMin(self, a1):
        v1, v2 = (0, len(a1) - 1)
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if a1[v3] > a1[v2]:
                v1 = v3 + 1
            else:
                v2 = v3
        return a1[v1]
