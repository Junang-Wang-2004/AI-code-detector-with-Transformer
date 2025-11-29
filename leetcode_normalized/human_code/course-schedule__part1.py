import collections

class C1(object):

    def canFinish(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = collections.Counter()
        for v3, v4 in a2:
            v2[v3] += 1
            v1[v4].append(v3)
        v5 = []
        v6 = [v3 for v3 in range(a1) if v3 not in v2]
        while v6:
            v7 = []
            for v3 in v6:
                v5.append(v3)
                for v4 in v1[v3]:
                    v2[v4] -= 1
                    if v2[v4] == 0:
                        v7.append(v4)
            v6 = v7
        return len(v5) == a1
