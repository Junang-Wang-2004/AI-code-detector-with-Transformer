import collections

class C1(object):

    def findMinHeightTrees(self, a1, a2):
        """
        """
        if a1 == 1:
            return [0]
        v1 = collections.defaultdict(set)
        for v2, v3 in a2:
            v1[v2].add(v3)
            v1[v3].add(v2)
        v4, v5 = ([], set())
        for v6 in range(a1):
            if len(v1[v6]) == 1:
                v4.append(v6)
            v5.add(v6)
        while len(v5) > 2:
            v7 = []
            for v2 in v4:
                v5.remove(v2)
                for v3 in v1[v2]:
                    if v3 in v5:
                        v1[v3].remove(v2)
                        if len(v1[v3]) == 1:
                            v7.append(v3)
            v4 = v7
        return list(v5)
