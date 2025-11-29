class C1:

    def arraysIntersection(self, a1, a2, a3):
        v1 = []
        v2, v3, v4 = (0, 0, 0)
        while v2 < len(a1) and v3 < len(a2) and (v4 < len(a3)):
            if a1[v2] == a2[v3] == a3[v4]:
                v1.append(a1[v2])
                v2 += 1
                v3 += 1
                v4 += 1
            else:
                v5 = min(a1[v2], a2[v3], a3[v4])
                if a1[v2] == v5:
                    v2 += 1
                if a2[v3] == v5:
                    v3 += 1
                if a3[v4] == v5:
                    v4 += 1
        return v1
