import itertools

class C1(object):

    def minNumberOfSemesters(self, a1, a2, a3):
        """
        """
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v3 - 1] |= 1 << v2 - 1
        v4 = [a1] * (1 << a1)
        v4[0] = 0
        for v5 in range(1 << a1):
            v6 = []
            for v3 in range(a1):
                if v5 & 1 << v3 == 0 and v5 & v1[v3] == v1[v3]:
                    v6.append(v3)
            for v7 in itertools.combinations(v6, min(len(v6), a3)):
                v8 = v5
                for v3 in v7:
                    v8 |= 1 << v3
                v4[v8] = min(v4[v8], v4[v5] + 1)
        return v4[-1]
