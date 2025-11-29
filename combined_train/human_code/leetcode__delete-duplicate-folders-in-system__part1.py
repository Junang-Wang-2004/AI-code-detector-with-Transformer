import collections
from functools import reduce

class C1(object):

    def deleteDuplicateFolder(self, a1):
        """
        """

        def mark(a1, a2, a3):
            v1 = []
            for v2, v3 in a1.items():
                if v3 == '_del':
                    continue
                v1.append((v2, mark(v3, a2, a3)))
            v1.sort()
            v4 = a3[tuple(v1)]
            if v4:
                if v4 in a2:
                    a2[v4]['_del']
                    a1['_del']
                else:
                    a2[v4] = a1
            return v4

        def sweep(a1, a2, a3, a4):
            if a3:
                a4.append([a2[i] for v1 in a3])
            for v2, v3 in a1.items():
                if '_del' in v3:
                    continue
                a3.append(v2)
                sweep(v3, a2, a3, a4)
                a3.pop()
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        v3 = collections.defaultdict()
        v3.default_factory = v3.__len__
        v4 = {}
        for v5 in a1:
            v6 = v2
            for v7 in v5:
                if v3[v7] not in v4:
                    v4[v3[v7]] = v7
                v6 = v6[v3[v7]]
        v8 = collections.defaultdict()
        v8.default_factory = v8.__len__
        mark(v2, {}, v8)
        v9 = []
        sweep(v2, v4, [], v9)
        return v9
