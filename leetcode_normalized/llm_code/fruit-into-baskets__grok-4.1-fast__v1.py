class C1(object):

    def totalFruit(self, a1):
        v1 = {}
        v2 = 0
        v3 = 0
        for v4 in range(len(a1)):
            v1[a1[v4]] = v4
            if len(v1) > 2:
                v5 = min(v1, key=v1.get)
                v6 = v1[v5]
                del v1[v5]
                v2 = v6 + 1
            v3 = max(v3, v4 - v2 + 1)
        return v3
