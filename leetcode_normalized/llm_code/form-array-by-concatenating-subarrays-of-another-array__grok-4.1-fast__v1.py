class C1(object):

    def canChoose(self, a1, a2):
        v1 = 0
        v2 = 0
        for v3 in a2:
            if v1 < len(a1) and v3 == a1[v1][v2]:
                v2 += 1
                if v2 == len(a1[v1]):
                    v1 += 1
                    v2 = 0
        return v1 == len(a1)
