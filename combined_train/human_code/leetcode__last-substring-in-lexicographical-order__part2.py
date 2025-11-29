import collections

class C1(object):

    def lastSubstring(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            v1[a1[v2]].append(v2)
        v3 = max(v1.keys())
        v4 = {}
        for v2 in v1[v3]:
            v4[v2] = v2 + 1
        while len(v4) - 1 > 0:
            v5 = set()
            v6 = collections.defaultdict(list)
            for v7, v8 in v4.items():
                if v8 == len(a1):
                    v5.add(v7)
                    continue
                v6[a1[v8]].append(v7)
                if v8 in v4:
                    v5.add(v8)
            v9 = {}
            v3 = max(v6.keys())
            for v7 in v6[v3]:
                if v7 not in v5:
                    v9[v7] = v4[v7] + 1
            v4 = v9
        return a1[next(iter(v4.keys())):]
