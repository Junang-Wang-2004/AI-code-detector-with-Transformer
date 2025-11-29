class C1(object):

    def merge(self, a1, a2, a3, a4):
        v1 = a2 - 1
        v2 = a4 - 1
        v3 = a2 + a4 - 1
        while v1 >= 0 or v2 >= 0:
            if v2 < 0:
                a1[v3] = a1[v1]
                v1 -= 1
            elif v1 < 0:
                a1[v3] = a3[v2]
                v2 -= 1
            elif a1[v1] > a3[v2]:
                a1[v3] = a1[v1]
                v1 -= 1
            else:
                a1[v3] = a3[v2]
                v2 -= 1
            v3 -= 1
