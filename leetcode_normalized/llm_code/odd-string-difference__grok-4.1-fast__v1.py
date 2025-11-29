class C1(object):

    def oddString(self, a1):
        v1 = {}
        v2 = len(a1[0]) - 1
        for v3 in a1:
            v4 = ','.join((str(ord(v3[j + 1]) - ord(v3[j])) for v5 in range(v2)))
            v1.setdefault(v4, []).append(v3)
        for v6 in v1.values():
            if len(v6) == 1:
                return v6[0]
