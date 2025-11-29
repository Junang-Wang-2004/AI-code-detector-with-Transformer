class C1(object):

    def groupStrings(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = ord(v2[0])
            v4 = tuple(((ord(char) - v3) % 26 for v5 in v2))
            v1.setdefault(v4, []).append(v2)
        return [sorted(items) for v6 in v1.values()]
