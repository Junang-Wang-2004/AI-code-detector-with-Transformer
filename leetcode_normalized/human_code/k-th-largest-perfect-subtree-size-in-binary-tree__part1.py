import random

class C1(object):

    def kthLargestPerfectSubtree(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3, a4, a5=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4):
                v1 = a2
                while v1 <= a3:
                    if a5(a1[v1], a4):
                        a1[v1], a1[a2] = (a1[a2], a1[v1])
                        a2 += 1
                        v1 += 1
                    elif a5(a4, a1[v1]):
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                    else:
                        v1 += 1
                return (a2, a3)
            while a2 <= a4:
                v1 = random.randint(a2, a4)
                v2, v3 = tri_partition(a1, a2, a4, a1[v1])
                if v2 <= a3 <= v3:
                    return
                elif v2 > a3:
                    a4 = v2 - 1
                else:
                    a2 = v3 + 1

        def iter_dfs():
            v1 = []
            v2 = [(1, (a1, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    if not v5:
                        v6[0] = 0
                        v1.append(v6[0])
                        continue
                    v7 = [[0] for v8 in range(2)]
                    v2.append((2, (v5, v7, v6)))
                    v2.append((1, (v5.right, v7[1])))
                    v2.append((1, (v5.left, v7[0])))
                elif v3 == 2:
                    v5, v7, v6 = v4
                    v6[0] = v7[0][0] + v7[1][0] + 1 if v7[0][0] == v7[1][0] != -1 else -1
                    v1.append(v6[0])
            return v1
        v1 = iter_dfs()
        nth_element(v1, 0, a2 - 1, len(v1) - 1, lambda a, b: a > b)
        return v1[a2 - 1] if a2 - 1 < len(v1) and v1[a2 - 1] > 0 else -1
