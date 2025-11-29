import random

class C1(object):
    v1 = {}

    def getKth(self, a1, a2, a3):
        """
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def partition_around_pivot(a1, a2, a3, a4, a5):
                v1 = a1
                a4[a3], a4[a2] = (a4[a2], a4[a3])
                for v2 in range(a1, a2):
                    if a5(a4[v2], a4[a2]):
                        a4[v2], a4[v1] = (a4[v1], a4[v2])
                        v1 += 1
                a4[a2], a4[v1] = (a4[v1], a4[a2])
                return v1
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4 = partition_around_pivot(v1, v2, v3, a1, a3)
                if v4 == a2:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v4 + 1

        def power_value(a1):
            v1, v2 = (a1, 0)
            while a1 > 1 and a1 not in C1.dp:
                v2 += 1
                if a1 % 2:
                    a1 = 3 * a1 + 1
                else:
                    a1 //= 2
            C1.dp[v1] = v2 + (C1.dp[a1] if a1 > 1 else 0)
            return (C1.dp[v1], v1)
        v1 = list(map(power_value, list(range(a1, a2 + 1))))
        nth_element(v1, a3 - 1)
        return v1[a3 - 1][1]
