class C1(object):

    def duplicateZeros(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            if v3 + v2 >= v1:
                v4 = v3 - 1
                break
            if a1[v3] == 0:
                v2 += 1
        else:
            v4 = v1 - 1
        while v4 >= 0:
            if v4 + v2 < v1:
                a1[v4 + v2] = a1[v4]
            if a1[v4] == 0:
                v2 -= 1
                a1[v4 + v2] = a1[v4]
            v4 -= 1
