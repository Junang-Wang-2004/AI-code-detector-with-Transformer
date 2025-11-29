import collections

class C1(object):

    def applySubstitutions(self, a1, a2):
        """
        """

        def find_adj(a1):
            v1 = set()
            v2 = 0
            while v2 < len(a1):
                if a1[v2] != '%':
                    v2 += 1
                    continue
                v3 = next((v3 for v3 in range(v2 + 1, len(a1)) if a1[v3] == '%'))
                v1.add(a1[v2 + 1:v3])
                v2 = v3 + 1
            return v1

        def replace(a1):
            v1 = []
            v2 = 0
            while v2 < len(a1):
                if a1[v2] != '%':
                    v1.append(a1[v2])
                    v2 += 1
                    continue
                v3 = next((v3 for v3 in range(v2 + 1, len(a1)) if a1[v3] == '%'))
                v1.append(lookup[a1[v2 + 1:v3]])
                v2 = v3 + 1
            return ''.join(v1)

        def topological_sort():
            v1 = collections.defaultdict(set)
            v2 = collections.defaultdict(int)
            for v3, v4 in a1:
                for v5 in find_adj(v4):
                    v1[v5].add(v3)
                    v2[v3] += 1
            v6 = []
            v7 = [v3 for v3, v8 in a1 if not v2[v3]]
            while v7:
                v9 = []
                for v3 in v7:
                    lookup[v3] = replace(lookup[v3])
                    for v5 in v1[v3]:
                        v2[v5] -= 1
                        if v2[v5]:
                            continue
                        v9.append(v5)
                v7 = v9
            return v6
        v1 = {k: v for v2, v3 in a1}
        topological_sort()
        return replace(a2)
