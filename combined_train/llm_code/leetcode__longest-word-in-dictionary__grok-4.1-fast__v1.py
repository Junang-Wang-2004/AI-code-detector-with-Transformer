class C1:

    def longestWord(self, a1):
        v1 = {}
        for v2 in a1:
            v3 = v1
            for v4 in v2:
                v3 = v3.setdefault(v4, {})
            v3['#'] = v2
        v5 = ['']

        def explore(a1):
            if '#' in a1:
                v1 = a1['#']
                if len(v1) > len(v5[0]) or (len(v1) == len(v5[0]) and v1 < v5[0]):
                    v5[0] = v1
                for v2 in a1:
                    if v2 != '#':
                        explore(a1[v2])
        for v6 in v1.values():
            explore(v6)
        return v5[0]
