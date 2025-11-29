import random

class C1(object):

    def maximizeSumOfWeights(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4):
                v1 = a2
                while v1 <= a3:
                    if a3(a1[v1], a4):
                        a1[v1], a1[a2] = (a1[a2], a1[v1])
                        a2 += 1
                        v1 += 1
                    elif a3(a4, a1[v1]):
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                    else:
                        v1 += 1
                return (a2, a3)
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4, v5 = tri_partition(a1, v1, v2, a1[v3])
                if v4 <= a2 <= v5:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v5 + 1

        def iter_dfs():
            v1 = [[0] * 2 for v2 in range(len(adj))]
            v3 = [(1, 0, -1)]
            while v3:
                v4, v5, v6 = v3.pop()
                if v4 == 1:
                    v3.append((2, v5, v6))
                    for v7, v8 in reversed(adj[v5]):
                        if v7 == v6:
                            continue
                        v3.append((1, v7, v5))
                elif v4 == 2:
                    v9 = 0
                    v10 = []
                    for v7, v8 in adj[v5]:
                        if v7 == v6:
                            continue
                        v9 += v1[v7][0]
                        v10.append(max(v1[v7][1] + v8 - v1[v7][0], 0))
                    if a2 - 1 < len(v10):
                        nth_element(v10, a2 - 1, lambda a, b: a > b)
                    v1[v5][0] = v9 + sum((v10[i] for v11 in range(min(a2, len(v10)))))
                    v1[v5][1] = v9 + sum((v10[v11] for v11 in range(min(a2 - 1, len(v10)))))
            return v1[0][0]
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return iter_dfs()
