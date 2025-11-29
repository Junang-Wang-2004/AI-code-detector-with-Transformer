class C1:

    def isPrefixString(self, a1, a2):
        v1 = 0
        v2 = len(a1)
        for v3 in a2:
            v4 = len(v3)
            if v1 + v4 > v2 or a1[v1:v1 + v4] != v3:
                return False
            v1 += v4
            if v1 == v2:
                return True
        return v1 == v2
