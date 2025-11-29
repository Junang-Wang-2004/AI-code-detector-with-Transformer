import collections

class C1:

    def deleteDuplicateFolder(self, a1):
        v1 = lambda: collections.defaultdict(v1)
        v2 = v1()
        for v3 in a1:
            v4 = v2
            for v5 in v3:
                v4 = v4[v5]
        v6 = {}

        def get_structure_signature(a1):
            v1 = []
            for v2, v3 in sorted(a1.items()):
                if '_remove' in v3:
                    continue
                v4 = get_structure_signature(v3)
                v1.append((v2, v4))
            v5 = tuple(v1)
            if v5:
                if v5 in v6:
                    v6[v5]['_remove'] = True
                    a1['_remove'] = True
                else:
                    v6[v5] = a1
            return v5
        get_structure_signature(v2)
        v7 = []

        def traverse(a1, a2):
            for v1, v2 in a1.items():
                if '_remove' in v2:
                    continue
                a2.append(v1)
                v7.append(list(a2))
                traverse(v2, a2)
                a2.pop()
        traverse(v2, [])
        return v7
