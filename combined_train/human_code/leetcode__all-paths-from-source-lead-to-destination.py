import collections

class C1(object):

    def leadsToDestination(self, a1, a2, a3, a4):
        """
        """
        v1, v2, v3 = list(range(3))

        def dfs(a1, a2, a3, a4):
            if a4[a2] == v3:
                return True
            if a4[a2] == v2:
                return False
            a4[a2] = v2
            if a2 not in a1 and a2 != a3:
                return False
            if a2 in a1:
                for v1 in a1[a2]:
                    if not dfs(a1, v1, a3, a4):
                        return False
            a4[a2] = v3
            return True
        v4 = collections.defaultdict(list)
        for v5, v6 in a2:
            v4[v5].append(v6)
        return dfs(v4, a3, a4, [0] * a1)
