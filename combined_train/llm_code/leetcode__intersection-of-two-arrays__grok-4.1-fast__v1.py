class C1:

    def intersection(self, a1, a2):
        a1.sort()
        a2.sort()
        v1 = []
        v2, v3 = (0, 0)
        v4, v5 = (len(a1), len(a2))
        while v2 < v4 and v3 < v5:
            if a1[v2] == a2[v3]:
                v1.append(a1[v2])
                v6 = a1[v2]
                while v2 < v4 and a1[v2] == v6:
                    v2 += 1
                while v3 < v5 and a2[v3] == v6:
                    v3 += 1
            elif a1[v2] < a2[v3]:
                v2 += 1
            else:
                v3 += 1
        return v1
