class C1(object):

    def jump(self, a1):
        v1 = 0
        v2 = 0
        v3 = 0
        for v4, v5 in enumerate(a1):
            if v4 > v2:
                return -1
            if v4 > v3:
                v3 = v2
                v1 += 1
            v2 = max(v2, v4 + v5)
        return v1
