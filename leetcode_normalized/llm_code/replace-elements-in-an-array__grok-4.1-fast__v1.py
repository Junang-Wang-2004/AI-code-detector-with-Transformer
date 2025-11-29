class C1(object):

    def arrayChange(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a1):
            v1[v3] = v2
        for v4 in a2:
            v5, v6 = v4
            v1[v6] = v1.pop(v5)
        for v3, v2 in v1.items():
            a1[v2] = v3
        return a1
