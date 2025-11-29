class C1(object):

    def applyOperations(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        while v3 < v1:
            if v3 + 1 < v1 and a1[v3] == a1[v3 + 1]:
                a1[v2] = a1[v3] * 2
                v2 += 1
                v3 += 2
            else:
                a1[v2] = a1[v3]
                v2 += 1
                v3 += 1
        while v2 < v1:
            a1[v2] = 0
            v2 += 1
        return a1
