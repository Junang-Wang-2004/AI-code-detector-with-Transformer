class C1(object):

    def minimumOneBitOperations(self, a1):
        v1 = 0
        v2 = 0
        for v3 in range(31, -1, -1):
            v4 = a1 >> v3 & 1 ^ v2
            if v4:
                v1 |= 1 << v3
            v2 = v4
        return v1
