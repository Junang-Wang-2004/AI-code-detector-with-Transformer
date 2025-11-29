import collections

class C1:

    def beforeAndAfterPuzzles(self, a1):
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v4 = v3.split()
            if v4:
                v1[v4[-1]].append(v2)
        v5 = set()
        for v6, v3 in enumerate(a1):
            v4 = v3.split()
            if not v4:
                continue
            v7 = v4[0]
            v8 = ' '.join(v4[1:])
            v9 = ' ' if v8 else ''
            for v10 in v1[v7]:
                if v10 == v6:
                    continue
                v5.add(a1[v10] + v9 + v8)
        return sorted(v5)
