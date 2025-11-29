class C1(object):

    def isOneEditDistance(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        if abs(v1 - v2) > 1:
            return False
        v3, v4 = (0, 0)
        while v3 < v1 and v4 < v2:
            if a1[v3] != a2[v4]:
                if v1 == v2:
                    return a1[v3 + 1:] == a2[v4 + 1:]
                return a1[v3:] == a2[v4 + 1:] if v1 < v2 else a1[v3 + 1:] == a2[v4:]
            v3 += 1
            v4 += 1
        return abs(v1 - v2) == 1
