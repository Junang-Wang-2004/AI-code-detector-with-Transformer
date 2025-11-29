class C1(object):

    def lastSubstring(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 1
        while v3 < v1:
            v4 = 0
            while v2 + v4 < v1 and v3 + v4 < v1 and (a1[v2 + v4] == a1[v3 + v4]):
                v4 += 1
            if v3 + v4 == v1 or (v2 + v4 < v1 and a1[v2 + v4] > a1[v3 + v4]):
                v3 += v4 + 1
            else:
                v2 = max(v2 + v4 + 1, v3)
                v3 = v2 + 1
        return a1[v2:]
