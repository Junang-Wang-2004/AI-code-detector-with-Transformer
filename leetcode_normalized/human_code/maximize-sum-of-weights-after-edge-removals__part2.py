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

        def dfs(a1, a2):
            v1 = 0
            v2 = []
            for v3, v4 in adj[a1]:
                if v3 == a2:
                    continue
                v5 = dfs(v3, a1)
                v1 += v5[0]
                v2.append(max(v5[1] + v4 - v5[0], 0))
            if a2 - 1 < len(v2):
                nth_element(v2, a2 - 1, lambda a, b: a > b)
            return (v1 + sum((v2[i] for v6 in range(min(a2, len(v2))))), v1 + sum((v2[v6] for v6 in range(min(a2 - 1, len(v2))))))
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return dfs(0, -1)[0]
