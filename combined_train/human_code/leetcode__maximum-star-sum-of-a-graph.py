import random

class C1(object):

    def maxStarSum(self, a1, a2, a3):
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
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            if a1[v4] > 0:
                v1[v3].append(v4)
            if a1[v3] > 0:
                v1[v4].append(v3)
        v5 = float('-inf')
        for v3 in range(len(a1)):
            if 1 <= a3 <= len(v1[v3]):
                nth_element(v1[v3], a3 - 1, lambda a, b: a1[a] > a1[b])
            v5 = max(v5, a1[v3] + sum((a1[v1[v3][i]] for v6 in range(min(a3, len(v1[v3]))))))
        return v5
