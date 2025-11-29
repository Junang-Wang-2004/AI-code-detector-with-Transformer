import collections

class C1(object):

    def numMatchingSubseq(self, a1, a2):
        v1 = collections.defaultdict(list)
        v2 = 0
        for v3, v4 in enumerate(a2):
            if v4:
                v1[v4[0]].append((v3, 0))
            else:
                v2 += 1
        for v5 in a1:
            v6 = v1[v5]
            v1[v5] = []
            for v3, v7 in v6:
                v8 = v7 + 1
                if v8 == len(a2[v3]):
                    v2 += 1
                else:
                    v9 = a2[v3][v8]
                    v1[v9].append((v3, v8))
        return v2
