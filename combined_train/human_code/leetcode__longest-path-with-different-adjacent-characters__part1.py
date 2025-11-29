import collections

class C1(object):

    def longestPath(self, a1, a2):
        """
        """

        def topological_sort(a1, a2, a3):
            v1 = 1
            v2 = collections.defaultdict(lambda: [0] * 2)
            v3 = [(i, 1) for v4, v5 in enumerate(a3) if not v5]
            while v3:
                v6 = []
                for v7, v8 in v3:
                    for v9 in a2[v7]:
                        if a1[v9] != a1[v7]:
                            if v8 > v2[v9][0]:
                                v2[v9][0], v2[v9][1] = (v8, v2[v9][0])
                            elif v8 > v2[v9][1]:
                                v2[v9][1] = v8
                        a3[v9] -= 1
                        if a3[v9]:
                            continue
                        v6.append((v9, v2[v9][0] + 1))
                        v1 = max(v1, v2[v9][0] + v2[v9][1] + 1)
                        del v2[v9]
                v3 = v6
            return v1
        v1 = [[] for v2 in range(len(a2))]
        v3 = [0] * len(a2)
        for v4 in range(1, len(a1)):
            v1[v4].append(a1[v4])
            v3[a1[v4]] += 1
        return topological_sort(a2, v1, v3)
