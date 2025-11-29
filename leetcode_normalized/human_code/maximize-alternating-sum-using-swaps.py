import random

class C1(object):

    def maxAlternatingSum(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4, v5 = tri_partition(a1, v1, v2, a1[v3], a3)
                if v4 <= a2 <= v5:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v5 + 1

        def bfs(a1):
            v1 = []
            if lookup[a1]:
                return v1
            lookup[a1] = True
            v1.append(a1)
            for a1 in v1:
                for v3 in adj[a1]:
                    if lookup[v3]:
                        continue
                    lookup[v3] = True
                    v1.append(v3)
            return v1
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * len(v1)
        v6 = sum(a1)
        for v7 in range(len(a1)):
            v8 = bfs(v7)
            if not v8:
                continue
            v9 = sum((v3 % 2 for v3 in v8))
            v10 = [a1[v3] for v3 in v8]
            nth_element(v10, v9)
            v6 -= 2 * sum((v10[v3] for v3 in range(v9)))
        return v6
