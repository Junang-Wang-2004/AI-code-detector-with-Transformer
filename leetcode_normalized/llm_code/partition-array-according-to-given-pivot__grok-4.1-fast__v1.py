class C1(object):

    def pivotArray(self, a1, a2):
        v1 = []
        v2 = []
        for v3 in a1:
            if v3 < a2:
                v1.append(v3)
            elif v3 > a2:
                v2.append(v3)
        v4 = len(a1) - len(v1) - len(v2)
        return v1 + [a2] * v4 + v2
