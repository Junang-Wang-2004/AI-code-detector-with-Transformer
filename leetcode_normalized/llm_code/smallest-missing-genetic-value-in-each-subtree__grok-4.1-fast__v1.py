class C1(object):

    def smallestMissingValueSubtree(self, a1, a2):
        v1 = len(a1)
        v2 = [1] * v1
        v3 = -1
        for v4 in range(v1):
            if a2[v4] == 1:
                v3 = v4
                break
        if v3 == -1:
            return v2
        v5 = [[] for v6 in range(v1)]
        for v7 in range(1, v1):
            v5[a1[v7]].append(v7)
        v8 = set()
        v9 = v3
        v10 = -1
        while v9 >= 0:
            if a2[v9] not in v8:
                v8.add(a2[v9])
            for v11 in v5[v9]:
                if v11 == v10:
                    continue
                v12 = [v11]
                while v12:
                    v13 = v12.pop()
                    if a2[v13] in v8:
                        continue
                    v8.add(a2[v13])
                    for v14 in v5[v13]:
                        v12.append(v14)
            v15 = 1
            while v15 in v8:
                v15 += 1
            v2[v9] = v15
            v10 = v9
            v9 = a1[v9]
        return v2
