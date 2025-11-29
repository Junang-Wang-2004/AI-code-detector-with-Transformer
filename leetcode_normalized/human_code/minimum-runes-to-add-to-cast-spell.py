def f1(a1):

    def strongconnect(a1):
        index[a1] = index_counter[0]
        lowlinks[a1] = index_counter[0]
        index_counter[0] += 1
        stack_set[a1] = True
        stack.append(a1)
        for v1 in a1[a1]:
            if index[v1] == -1:
                strongconnect(v1)
                lowlinks[a1] = min(lowlinks[a1], lowlinks[v1])
            elif stack_set[v1]:
                lowlinks[a1] = min(lowlinks[a1], index[v1])
        if lowlinks[a1] == index[a1]:
            v2 = []
            v1 = None
            while v1 != a1:
                v1 = stack.pop()
                stack_set[v1] = False
                v2.append(v1)
            result.append(v2)
    v1, v2, v3 = ([0], [-1] * len(a1), [-1] * len(a1))
    v4, v5 = ([], [False] * len(a1))
    v6 = []
    for v7 in range(len(a1)):
        if v2[v7] == -1:
            strongconnect(v7)
    return v6

class C1(object):

    def minRunesToAdd(self, a1, a2, a3, a4):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3 in range(len(a3)):
            v1[a3[v3]].append(a4[v3])
        v4 = [-1] * a1
        v5 = f1(v1)
        for v3, v6 in enumerate(v5):
            for v7 in v6:
                v4[v7] = v3
        v8 = [False] * len(v5)
        for v9 in range(a1):
            for v10 in v1[v9]:
                if v4[v10] != v4[v9]:
                    v8[v4[v10]] = True
        for v7 in a2:
            v8[v4[v7]] = True
        return sum((not v7 for v7 in v8))
