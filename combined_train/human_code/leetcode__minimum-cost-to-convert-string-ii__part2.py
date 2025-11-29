import collections
import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

        def floydWarshall(a1):
            for v1 in range(len(a1)):
                for v2 in range(len(a1)):
                    if a1[v2][v1] == v1:
                        continue
                    for v3 in range(len(a1[v2])):
                        if a1[v1][v3] == v1:
                            continue
                        a1[v2][v3] = min(a1[v2][v3], a1[v2][v1] + a1[v1][v3])
        v2 = collections.defaultdict(dict)
        for v3 in itertools.chain(a3, a4):
            v4 = len(v3)
            v5 = v2[v4]
            if v3 not in v5:
                v5[v3] = len(v5)
        v6 = {v4: [[0 if u == v else v1 for v7 in range(len(v5))] for v8 in range(len(v5))] for v4, v5 in v2.items()}
        for v9 in range(len(a3)):
            v4 = len(a3[v9])
            v5, v10 = (v2[v4], v6[v4])
            v8, v7 = (v5[a3[v9]], v5[a4[v9]])
            v10[v8][v7] = min(v10[v8][v7], a5[v9])
        for v10 in v6.values():
            floydWarshall(v10)
        v11 = {len(v3) for v3 in a3}
        v12 = [v1] * (max((len(v3) for v3 in a3)) + 1)
        v12[0] = 0
        for v9 in range(len(a1)):
            if v12[v9 % len(v12)] == v1:
                continue
            if a1[v9] == a2[v9]:
                v12[(v9 + 1) % len(v12)] = min(v12[(v9 + 1) % len(v12)], v12[v9 % len(v12)])
            for v4 in v11:
                if v9 + v4 > len(a1):
                    continue
                v5, v10 = (v2[v4], v6[v4])
                v8, v7 = (a1[v9:v9 + v4], a2[v9:v9 + v4])
                if v8 in v5 and v7 in v5:
                    v12[(v9 + v4) % len(v12)] = min(v12[(v9 + v4) % len(v12)], v12[v9 % len(v12)] + v10[v5[v8]][v5[v7]])
            v12[v9 % len(v12)] = v1
        return v12[len(a1) % len(v12)] if v12[len(a1) % len(v12)] != v1 else -1
