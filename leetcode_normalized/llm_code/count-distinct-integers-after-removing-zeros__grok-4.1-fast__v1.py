class C1(object):

    def countDistinct(self, a1):
        v1 = str(a1)
        v2 = len(v1)
        v3 = 0
        v4 = 1
        for v5 in range(1, v2):
            v4 *= 9
            v3 += v4
        v6 = v4
        for v7 in range(v2):
            v8 = int(v1[v7])
            if v8 == 0:
                break
            v3 += (v8 - 1) * v6
            v6 //= 9
        else:
            v3 += 1
        return v3
