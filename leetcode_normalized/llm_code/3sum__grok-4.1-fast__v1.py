class C1:

    def threeSum(self, a1):
        v1 = []
        v2 = sorted(a1)
        v3 = len(v2)
        for v4 in range(v3 - 2):
            if v4 > 0 and v2[v4] == v2[v4 - 1]:
                continue
            v5 = v4 + 1
            v6 = v3 - 1
            while v5 < v6:
                v7 = v2[v4] + v2[v5] + v2[v6]
                if v7 == 0:
                    v1.append([v2[v4], v2[v5], v2[v6]])
                    v5 += 1
                    v6 -= 1
                    while v5 < v6 and v2[v5] == v2[v5 - 1]:
                        v5 += 1
                    while v5 < v6 and v2[v6] == v2[v6 + 1]:
                        v6 -= 1
                elif v7 < 0:
                    v5 += 1
                else:
                    v6 -= 1
        return v1
