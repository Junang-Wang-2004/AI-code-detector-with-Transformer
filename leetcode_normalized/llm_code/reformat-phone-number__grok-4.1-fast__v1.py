class C1(object):

    def reformatNumber(self, a1):
        v1 = ''.join((c for v2 in a1 if v2.isdigit()))
        v3 = len(v1)
        v4 = []
        v5 = 0
        while v5 < v3:
            v6 = v3 - v5
            if v6 == 4:
                v4.append(v1[v5:v5 + 2])
                v4.append(v1[v5 + 2:])
                v5 = v3
            else:
                v7 = min(3, v6)
                v4.append(v1[v5:v5 + v7])
                v5 += v7
        return '-'.join(v4)
