class C1(object):

    def areAlmostEqual(self, a1, a2):
        v1 = []
        for v2 in range(len(a1)):
            if a1[v2] != a2[v2]:
                v1.append(v2)
                if len(v1) > 2:
                    return False
        if len(v1) == 0:
            return True
        if len(v1) != 2:
            return False
        v3, v4 = v1
        return a1[v3] == a2[v4] and a1[v4] == a2[v3]
