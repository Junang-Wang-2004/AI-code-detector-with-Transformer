class C1(object):

    def numberOfWeakCharacters(self, a1):
        """
        """
        a1.sort(cmp=lambda a, b: cmp(b[1], a[1]) if a[0] == b[0] else cmp(a[0], b[0]))
        v1 = v2 = 0
        for v3, v4 in reversed(a1):
            if v4 < v2:
                v1 += 1
            v2 = max(v2, v4)
        return v1
