class C1(object):

    def intersectionSizeTwo(self, a1):
        a1.sort(key=lambda t: (-t[0], t[1]))
        v1 = len(a1)
        v2 = [2] * v1
        v3 = 0
        for v4 in range(v1):
            v5, v6 = a1[v4]
            v7 = v2[v4]
            v3 += v7
            for v8 in range(v5, v5 + v7):
                for v9 in range(v4 + 1, v1):
                    if v2[v9] and v8 <= a1[v9][1]:
                        v2[v9] -= 1
        return v3
