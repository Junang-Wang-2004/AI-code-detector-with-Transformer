import itertools

class C1(object):

    def compareVersion(self, a1, a2):
        """
        """
        v1, v2 = (len(a1), len(a2))
        v3, v4 = (0, 0)
        while v3 < v1 or v4 < v2:
            v5, v6 = (0, 0)
            while v3 < v1 and a1[v3] != '.':
                v5 = v5 * 10 + int(a1[v3])
                v3 += 1
            while v4 < v2 and a2[v4] != '.':
                v6 = v6 * 10 + int(a2[v4])
                v4 += 1
            if v5 != v6:
                return 1 if v5 > v6 else -1
            v3 += 1
            v4 += 1
        return 0
