import collections

class C1(object):

    def checkWays(self, a1):
        v1 = collections.defaultdict(set)
        for v2, v3 in a1:
            v1[v2].add(v3)
            v1[v3].add(v2)
        v4 = len(v1)
        if v4 == 0:
            return 1
        v5 = sorted(v1, key=lambda nd: len(v1[nd]), reverse=True)
        v6 = set()
        v7 = v5[0]
        v6.add(v7)
        if len(v1[v7]) != v4 - 1:
            return 0
        v8 = False
        for v9 in v5[1:]:
            v6.add(v9)
            v10 = [nbr for v11 in v1[v9] if v11 in v6]
            if not v10:
                return 0
            v12 = min(v10, key=lambda nbr: len(v1[v11]))
            for v11 in v1[v9]:
                if v11 != v12 and v11 not in v1[v12]:
                    return 0
            if len(v1[v9]) == len(v1[v12]):
                v8 = True
        return 2 if v8 else 1
