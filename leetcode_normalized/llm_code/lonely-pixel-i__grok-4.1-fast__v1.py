class C1(object):

    def findLonelyPixel(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [r.count('B') for v4 in a1]
        v5 = [sum((v4[j] == 'B' for v4 in a1)) for v6 in range(v2)]
        return sum((a1[i][v6] == 'B' and v3[i] == 1 and (v5[v6] == 1) for v7 in range(v1) for v6 in range(v2)))
