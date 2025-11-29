class C1(object):

    def merge(self, a1, a2, a3, a4):
        v1, v2, v3 = (a2 + a4 - 1, a2 - 1, a4 - 1)
        while v2 >= 0 and v3 >= 0:
            if a1[v2] > a3[v3]:
                a1[v1] = a1[v2]
                v1, v2 = (v1 - 1, v2 - 1)
            else:
                a1[v1] = a3[v3]
                v1, v3 = (v1 - 1, v3 - 1)
        while v3 >= 0:
            a1[v1] = a3[v3]
            v1, v3 = (v1 - 1, v3 - 1)
