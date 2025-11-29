import collections

class C1(object):

    def calcEquation(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4):
            if a1 in a3 and a2 in a3[a1]:
                return (True, a3[a1][a2])
            for v1, v2 in a3[a1].items():
                if v1 not in a4:
                    a4.add(v1)
                    v3 = check(v1, a2, a3, a4)
                    if v3[0]:
                        return (True, v2 * v3[1])
            return (False, 0)
        v1 = collections.defaultdict(dict)
        for v2, v3 in enumerate(a1):
            v1[v3[0]][v3[1]] = a2[v2]
            if a2[v2]:
                v1[v3[1]][v3[0]] = 1.0 / a2[v2]
        v4 = []
        for v5 in a3:
            v6 = set()
            v7 = check(v5[0], v5[1], v1, v6)
            v4.append(v7[1] if v7[0] else -1)
        return v4
