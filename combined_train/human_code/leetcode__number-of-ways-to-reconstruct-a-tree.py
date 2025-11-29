import collections

class C1(object):

    def checkWays(self, a1):
        """
        """
        v1 = collections.defaultdict(set)
        for v2, v3 in a1:
            v1[v2].add(v3)
            v1[v3].add(v2)
        v4, v5 = (len(v1), False)
        v6 = set()
        for v7 in sorted(iter(v1.keys()), key=lambda i: len(v1[i]), reverse=True):
            v6.add(v7)
            v8 = 0
            for v2 in v1[v7]:
                if v2 not in v6:
                    continue
                if v8 == 0 or len(v1[v2]) < len(v1[v8]):
                    v8 = v2
            if v8:
                if any((True for v2 in v1[v7] if v2 != v8 and v2 not in v1[v8])):
                    return 0
                v5 |= len(v1[v8]) == len(v1[v7])
            elif len(v1[v7]) != v4 - 1:
                return 0
        return 1 + v5
