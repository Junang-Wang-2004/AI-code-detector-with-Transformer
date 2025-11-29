import collections

class C1(object):

    def isReflected(self, a1):
        """
        """
        if not a1:
            return True
        v1 = collections.defaultdict(set)
        v2, v3 = (float('inf'), float('-inf'))
        for v4 in a1:
            v1[v4[1]].add(v4[0])
            v2, v3 = (min(v2, v4[0]), max(v3, v4[0]))
        v5 = v2 + v3
        for v6 in list(v1.values()):
            for v7 in v6:
                if v5 - v7 not in v6:
                    return False
        return True
