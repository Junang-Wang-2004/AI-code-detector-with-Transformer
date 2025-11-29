class C1(object):

    def isPossibleDivide(self, a1, a2):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        for v3 in sorted(v1):
            v4 = v1.get(v3, 0)
            if v4 <= 0:
                continue
            for v5 in range(a2):
                v6 = v3 + v5
                if v1.get(v6, 0) < v4:
                    return False
                v1[v6] -= v4
        return True
