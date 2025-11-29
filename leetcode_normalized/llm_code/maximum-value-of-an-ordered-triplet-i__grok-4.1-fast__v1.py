class C1(object):

    def maximumTripletValue(self, a1):
        if len(a1) < 3:
            return 0
        v1 = 0
        v2, v3 = (a1[0], a1[1])
        v4 = max(v2, v3)
        v5 = v2 - v3
        for v6 in range(2, len(a1)):
            v7 = a1[v6]
            v1 = max(v1, v5 * v7)
            v5 = max(v5, v4 - v7)
            v4 = max(v4, v7)
        return v1
