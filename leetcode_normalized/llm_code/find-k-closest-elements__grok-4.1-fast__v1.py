class C1:

    def findClosestElements(self, a1, a2, a3):
        v1 = len(a1)
        v2, v3 = (0, v1 - a2)
        while v2 < v3:
            v4 = v2 + (v3 - v2) // 2
            if a3 - a1[v4] > a1[v4 + a2] - a3:
                v2 = v4 + 1
            else:
                v3 = v4
        return a1[v2:v2 + a2]
