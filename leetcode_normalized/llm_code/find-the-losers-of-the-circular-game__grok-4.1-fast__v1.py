class C1(object):

    def circularGameLosers(self, a1, a2):
        v1 = set()
        v2 = 0
        v3 = 1
        while v2 not in v1:
            v1.add(v2)
            v2 = (v2 + v3 * a2) % a1
            v3 += 1
        return [i + 1 for v4 in range(a1) if v4 not in v1]
