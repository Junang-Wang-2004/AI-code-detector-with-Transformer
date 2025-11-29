class C1:

    def visibleMountains(self, a1):
        a1.sort(key=lambda p: p[0] - p[1])
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v5 = a1[v3][0] - a1[v3][1]
            v6 = 0
            while v3 < v4 and a1[v3][0] - a1[v3][1] == v5:
                v7 = a1[v3][0] + a1[v3][1]
                if v7 > v6:
                    v6 = v7
                v3 += 1
            if v6 > v2:
                v1 += 1
                v2 = v6
        return v1
