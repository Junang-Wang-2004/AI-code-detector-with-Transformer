class C1(object):

    def sequenceReconstruction(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(set)
        v2 = collections.defaultdict(int)
        v3 = set()
        for v4 in a2:
            for v5 in v4:
                v3.add(v5)
            if len(v4) == 1:
                if v4[0] not in v2:
                    v2[v4[0]] = 0
                continue
            for v5 in range(len(v4) - 1):
                if v4[v5] not in v2:
                    v2[v4[v5]] = 0
                if v4[v5 + 1] not in v1[v4[v5]]:
                    v1[v4[v5]].add(v4[v5 + 1])
                    v2[v4[v5 + 1]] += 1
        v6 = 0
        v7 = []
        v8 = []
        for v5 in v2:
            if v2[v5] == 0:
                v6 += 1
                if v6 > 1:
                    return False
                v8.append(v5)
        while v8:
            v5 = v8.pop()
            v7.append(v5)
            v6 = 0
            for v9 in v1[v5]:
                v2[v9] -= 1
                if v2[v9] == 0:
                    v6 += 1
                    if v6 > 1:
                        return False
                    v8.append(v9)
        return v7 == a1 and len(a1) == len(v3)
