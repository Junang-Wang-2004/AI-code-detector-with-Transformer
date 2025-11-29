import random

class C1(object):

    def largestEvenSum(self, a1, a2):
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
        nth_element(a1, a2 - 1, compare=lambda a, b: a > b)
        v1 = sum((a1[i] for v2 in range(a2)))
        if v1 % 2 == 0:
            return v1
        v3 = [float('inf')] * 2
        for v2 in range(a2):
            v3[a1[v2] % 2] = min(v3[a1[v2] % 2], a1[v2])
        v4 = -1
        for v2 in range(a2, len(a1)):
            v4 = max(v4, v1 - v3[not a1[v2] % 2] + a1[v2])
        return v4
