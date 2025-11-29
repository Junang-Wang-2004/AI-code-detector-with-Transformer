import collections
import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

        def floydWarshall(a1):
            for v1 in a1.keys():
                for v2 in a1.keys():
                    if a1[v2][v1] == v1:
                        continue
                    for v3 in a1.keys():
                        if a1[v1][v3] == v1:
                            continue
                        a1[v2][v3] = min(a1[v2][v3], a1[v2][v1] + a1[v1][v3])
        v2 = {}
        v3 = collections.defaultdict(list)
        for v4 in itertools.chain(a3, a4):
            v5 = len(v4)
            if v4 in v2:
                continue
            v2[v4] = len(v2)
            v3[len(v4)].append(v2[v4])
        v6 = {v5: {u: {v: 0 if u == v else v1 for v7 in v2} for v8 in v2} for v5, v2 in v3.items()}
        for v9 in range(len(a3)):
            v5 = len(a3[v9])
            v10 = v6[v5]
            v8, v7 = (v2[a3[v9]], v2[a4[v9]])
            v10[v8][v7] = min(v10[v8][v7], a5[v9])
        for v10 in v6.values():
            floydWarshall(v10)
        v11 = {len(v4) for v4 in a3}
        v12 = [v1] * (max((len(v4) for v4 in a3)) + 1)
        v12[0] = 0
        for v9 in range(len(a1)):
            if v12[v9 % len(v12)] == v1:
                continue
            if a1[v9] == a2[v9]:
                v12[(v9 + 1) % len(v12)] = min(v12[(v9 + 1) % len(v12)], v12[v9 % len(v12)])
            for v5 in v11:
                if v9 + v5 > len(a1):
                    continue
                v10 = v6[v5]
                v8, v7 = (a1[v9:v9 + v5], a2[v9:v9 + v5])
                if v8 in v2 and v7 in v2:
                    v12[(v9 + v5) % len(v12)] = min(v12[(v9 + v5) % len(v12)], v12[v9 % len(v12)] + v10[v2[v8]][v2[v7]])
            v12[v9 % len(v12)] = v1
        return v12[len(a1) % len(v12)] if v12[len(a1) % len(v12)] != v1 else -1
