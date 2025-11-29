import collections
import itertools

class C1(object):

    def checkContradictions(self, a1, a2):
        """
        """

        def isclose(a1, a2, a3=1e-09, a4=0.0):
            return abs(a1 - a2) <= max(a3 * max(abs(a1), abs(a2)), a4)

        def iter_dfs(a1, a2, a3):
            v1 = [a2]
            a3[a2] = 1.0
            while v1:
                a2 = v1.pop()
                for v3, v4 in a1[a2]:
                    if v3 in a3:
                        if not isclose(a3[v3], a3[a2] * v4):
                            return True
                        continue
                    a3[v3] = a3[a2] * v4
                    v1.append(v3)
            return False
        v1 = collections.defaultdict(set)
        for (v2, v3), v4 in zip(a1, a2):
            v1[v2].add((v3, 1.0 / v4))
            v1[v3].add((v2, 1.0 * v4))
        v5 = {}
        for v6 in v1.keys():
            if v6 in v5:
                continue
            if iter_dfs(v1, v6, v5):
                return True
        return False
