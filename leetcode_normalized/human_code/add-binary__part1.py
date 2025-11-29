class C1(object):

    def addBinary(self, a1, a2):
        v1, v2, v3 = ('', 0, 0)
        for v4 in range(max(len(a1), len(a2))):
            v3 = v2
            if v4 < len(a1):
                v3 += int(a1[-(v4 + 1)])
            if v4 < len(a2):
                v3 += int(a2[-(v4 + 1)])
            v2, v3 = divmod(v3, 2)
            v1 += str(v3)
        if v2:
            v1 += str(v2)
        return v1[::-1]
