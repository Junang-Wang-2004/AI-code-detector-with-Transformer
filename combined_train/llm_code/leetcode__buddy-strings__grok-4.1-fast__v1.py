class C1(object):

    def buddyStrings(self, a1, a2):
        if len(a1) != len(a2):
            return False
        v1 = v2 = -1
        for v3 in range(len(a1)):
            if a1[v3] != a2[v3]:
                if v1 < 0:
                    v1 = v3
                elif v2 < 0:
                    v2 = v3
                else:
                    return False
        if v1 < 0:
            v4 = set()
            for v5 in a1:
                if v5 in v4:
                    return True
                v4.add(v5)
            return False
        if v2 < 0:
            return False
        return a1[v1] == a2[v2] and a1[v2] == a2[v1]
