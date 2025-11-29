def f1(a1):
    """Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens."""
    v1 = {}
    for v2 in a1:
        for v3 in a1[v2]:
            if v3 not in v1:
                v1[v3] = v2
                break
    while 1:
        v4 = {}
        v5 = []
        v6 = dict([(v2, v5) for v2 in a1])
        for v3 in v1:
            del v6[v1[v3]]
        v7 = list(v6)
        while v7 and (not v5):
            v8 = {}
            for v2 in v7:
                for v3 in a1[v2]:
                    if v3 not in v4:
                        v8.setdefault(v3, []).append(v2)
            v7 = []
            for v3 in v8:
                v4[v3] = v8[v3]
                if v3 in v1:
                    v7.append(v1[v3])
                    v6[v1[v3]] = v3
                else:
                    v5.append(v3)
        if not v5:
            v9 = {}
            for v2 in a1:
                for v3 in a1[v2]:
                    if v3 not in v4:
                        v9[v3] = None
            return (v1, list(v6), list(v9))

        def recurse(a1):
            if a1 in v4:
                v1 = v4[a1]
                del v4[a1]
                for v2 in v1:
                    if v2 in v6:
                        v3 = v6[v2]
                        del v6[v2]
                        if v3 is v5 or recurse(v3):
                            v1[a1] = v2
                            return 1
            return 0

        def recurse_iter(a1):

            def divide(a1):
                if a1 not in v4:
                    return
                v1 = v4[a1]
                del v4[a1]
                for v2 in v1:
                    if v2 in v6 and v6[v2] is v5:
                        del v6[v2]
                        v1[a1] = v2
                        ret[0] = True
                        return
                stk.append(partial(conquer, a1, iter(v1)))

            def conquer(a1, a2):
                for v1 in a2:
                    if v1 not in v6:
                        continue
                    v2 = v6[v1]
                    del v6[v1]
                    stk.append(partial(postprocess, a1, v1, a2))
                    stk.append(partial(divide, v2))
                    return

            def postprocess(a1, a2, a3):
                if not ret[0]:
                    stk.append(partial(conquer, a1, a3))
                    return
                v1[a1] = a2
            v1, v2 = ([False], [])
            v2.append(partial(divide, a1))
            while v2:
                v2.pop()()
            return v1[0]
        for v3 in v5:
            recurse_iter(v3)

class C1(object):

    def maxStudents(self, a1):
        """
        """
        v1 = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        v2, v3 = (collections.defaultdict(list), 0)
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if a1[v4][v5] != '.':
                    continue
                v3 += 1
                if v5 % 2:
                    continue
                for v6, v7 in v1:
                    v8, v9 = (v4 + v6, v5 + v7)
                    if 0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and (a1[v8][v9] == '.'):
                        v2[v4 * len(a1[0]) + v5].append(v8 * len(a1[0]) + v9)
        return v3 - len(f1(v2)[0])
