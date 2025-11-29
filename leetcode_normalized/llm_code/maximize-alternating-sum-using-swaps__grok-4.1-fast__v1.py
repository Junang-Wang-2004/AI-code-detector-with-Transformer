from collections import defaultdict

class C1(object):

    def maxAlternatingSum(self, a1, a2):
        v1 = len(a1)
        v2 = list(range(v1))
        v3 = [0] * v1

        def find(a1):
            if v2[a1] != a1:
                v2[a1] = find(v2[a1])
            return v2[a1]

        def union(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            if v3[v1] < v3[v2]:
                v2[v1] = v2
            elif v3[v1] > v3[v2]:
                v2[v2] = v1
            else:
                v2[v2] = v1
                v3[v1] += 1
        for v4, v5 in a2:
            union(v4, v5)
        v6 = defaultdict(list)
        for v7 in range(v1):
            v6[find(v7)].append(v7)
        v8 = sum(a1)
        v9 = 0
        for v10 in v6.values():
            v11 = sum((p % 2 for v12 in v10))
            v13 = sorted((a1[v12] for v12 in v10))
            v9 += sum(v13[:v11])
        return v8 - 2 * v9
