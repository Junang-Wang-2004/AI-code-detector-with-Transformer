import collections

class C1(object):

    def restoreArray(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in a1:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = next(([x, v1[x][0]] for v5 in v1 if len(v1[v5]) == 1))
        while len(v4) != len(a1) + 1:
            v4.append(v1[v4[-1]][v1[v4[-1]][0] == v4[-2]])
        return v4
