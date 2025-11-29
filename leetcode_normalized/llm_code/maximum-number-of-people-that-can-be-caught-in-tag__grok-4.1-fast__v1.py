class C1(object):

    def catchMaximumAmountofPeople(self, a1, a2):
        v1 = []
        v2 = []
        v3 = len(a1)
        for v4 in range(v3):
            if a1[v4] == 1:
                v1.append(v4)
            else:
                v2.append(v4)
        v5 = 0
        v6 = 0
        v7 = 0
        while v5 < len(v1) and v6 < len(v2):
            v8 = abs(v1[v5] - v2[v6])
            if v8 <= a2:
                v7 += 1
                v5 += 1
                v6 += 1
            elif v1[v5] < v2[v6]:
                v5 += 1
            else:
                v6 += 1
        return v7
