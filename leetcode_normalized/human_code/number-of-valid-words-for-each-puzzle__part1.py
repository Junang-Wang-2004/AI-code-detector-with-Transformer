class C1(object):

    def findNumOfValidWords(self, a1, a2):
        """
        """
        v1 = 7

        def search(a1, a2, a3, a4, a5):
            v1 = 0
            if '_end' in a1 and a5:
                v1 += a1['_end']
            for v2 in range(a3, len(a2)):
                if a2[v2] not in a1:
                    continue
                v1 += search(a1[a2[v2]], a2, v2 + 1, a4, a5 or a2[v2] == a4)
            return v1
        v2 = lambda: collections.defaultdict(v2)
        v3 = v2()
        for v4 in a1:
            v5 = set(v4)
            if len(v5) > v1:
                continue
            v4 = sorted(v5)
            v6 = reduce(dict.__getitem__, v4, v3)
            v6['_end'] = v6['_end'] + 1 if '_end' in v6 else 1
        v7 = []
        for v8 in a2:
            v9 = v8[0]
            v7.append(search(v3, sorted(v8), 0, v9, False))
        return v7
