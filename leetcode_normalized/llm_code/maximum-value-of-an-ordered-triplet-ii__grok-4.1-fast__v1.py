class C1(object):

    def maximumTripletValue(self, a1):
        if len(a1) < 3:
            return 0
        v1 = 0
        v2 = a1[0]
        v3 = v2 - a1[1]
        v2 = max(v2, a1[1])
        for v4 in a1[2:]:
            v1 = max(v1, v3 * v4)
            v3 = max(v3, v2 - v4)
            v2 = max(v2, v4)
        return v1
