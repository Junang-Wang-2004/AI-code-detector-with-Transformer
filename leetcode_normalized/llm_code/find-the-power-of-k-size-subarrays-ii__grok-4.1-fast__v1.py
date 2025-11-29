class C1(object):

    def resultsArray(self, a1, a2):
        v1 = len(a1)
        v2 = [-1] * (v1 - a2 + 1)
        v3 = 0
        for v4 in range(1, v1):
            if a1[v4] != a1[v4 - 1] + 1:
                v5 = v4 - v3
                if v5 >= a2:
                    for v6 in range(v3, v4 - a2 + 1):
                        v2[v6] = a1[v6 + a2 - 1]
                v3 = v4
        v5 = v1 - v3
        if v5 >= a2:
            for v6 in range(v3, v1 - a2 + 1):
                v2[v6] = a1[v6 + a2 - 1]
        return v2
