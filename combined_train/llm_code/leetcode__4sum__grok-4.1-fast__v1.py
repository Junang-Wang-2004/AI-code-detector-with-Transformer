class C1:

    def fourSum(self, a1, a2):
        a1.sort()
        v1 = []
        v2 = len(a1)
        for v3 in range(v2 - 3):
            if v3 > 0 and a1[v3] == a1[v3 - 1]:
                continue
            for v4 in range(v3 + 1, v2 - 2):
                if v4 > v3 + 1 and a1[v4] == a1[v4 - 1]:
                    continue
                v5 = a2 - a1[v3] - a1[v4]
                v6 = v4 + 1
                v7 = v2 - 1
                while v6 < v7:
                    v8 = a1[v6] + a1[v7]
                    if v8 == v5:
                        v1.append([a1[v3], a1[v4], a1[v6], a1[v7]])
                        v6 += 1
                        v7 -= 1
                        while v6 < v7 and a1[v6] == a1[v6 - 1]:
                            v6 += 1
                        while v6 < v7 and a1[v7] == a1[v7 + 1]:
                            v7 -= 1
                    elif v8 < v5:
                        v6 += 1
                    else:
                        v7 -= 1
        return v1
