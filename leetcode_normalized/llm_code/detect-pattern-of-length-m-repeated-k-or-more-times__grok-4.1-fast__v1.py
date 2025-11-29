class C1(object):

    def containsPattern(self, a1, a2, a3):
        v1 = len(a1)
        v2 = 0
        v3 = a2 * (a3 - 1)
        while v2 < v1 - a2:
            if a1[v2] != a1[v2 + a2]:
                v2 += 1
                continue
            v4 = v2
            while v2 < v1 - a2 and a1[v2] == a1[v2 + a2]:
                v2 += 1
            if v2 - v4 >= v3:
                return True
        return False
