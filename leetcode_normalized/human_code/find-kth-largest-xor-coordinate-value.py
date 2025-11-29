import random

class C1(object):

    def kthLargestValue(self, a1, a2):
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
        v1 = []
        for v2 in range(len(a1)):
            v3 = 0
            for v4 in range(len(a1[0])):
                v3 = v3 ^ a1[v2][v4]
                if v2 == 0:
                    a1[v2][v4] = v3
                else:
                    a1[v2][v4] = v3 ^ a1[v2 - 1][v4]
                v1.append(a1[v2][v4])
        nth_element(v1, a2 - 1, compare=lambda a, b: a > b)
        return v1[a2 - 1]
