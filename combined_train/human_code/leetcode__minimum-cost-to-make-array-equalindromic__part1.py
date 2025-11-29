import random

class C1(object):

    def minimumCost(self, a1):
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

        def nearest_palindromic(a1):
            v1 = str(a1)
            v2 = len(v1)
            v3 = {10 ** v2 + 1, 10 ** (v2 - 1) - 1}
            v4 = int(v1[:(v2 + 1) / 2])
            for v5 in map(str, (v4 - 1, v4, v4 + 1)):
                v3.add(int(v5 + [v5, v5[:-1]][v2 % 2][::-1]))
            return v3
        nth_element(a1, len(a1) // 2)
        v1 = a1[len(a1) // 2]
        if len(a1) % 2 == 0:
            nth_element(a1, len(a1) // 2 - 1)
            v1 = (v1 + a1[len(a1) // 2 - 1]) // 2
        return min((sum((abs(x - p) for v2 in a1)) for v3 in nearest_palindromic(v1)))
