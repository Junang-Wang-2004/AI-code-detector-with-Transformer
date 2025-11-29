class C1(object):

    def distinctNumbers(self, a1, a2):
        v1 = {}
        v2 = []
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4]
            if v5 in v1:
                v1[v5] += 1
            else:
                v1[v5] = 1
            if v4 >= a2 - 1:
                v2.append(len(v1))
                v6 = a1[v4 - a2 + 1]
                v1[v6] -= 1
                if v1[v6] == 0:
                    del v1[v6]
        return v2
