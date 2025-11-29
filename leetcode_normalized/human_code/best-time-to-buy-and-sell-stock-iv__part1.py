import random

class C1(object):

    def maxProfit(self, a1, a2):
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
        v2 = []
        v3, v4 = (-1, -1)
        while v4 + 1 < len(a2):
            for v3 in range(v4 + 1, len(a2) - 1):
                if a2[v3] < a2[v3 + 1]:
                    break
            else:
                v3 = len(a2) - 1
            for v4 in range(v3, len(a2) - 1):
                if a2[v4] > a2[v4 + 1]:
                    break
            else:
                v4 = len(a2) - 1
            while v2 and a2[v2[-1][0]] > a2[v3]:
                v5, v6 = v2.pop()
                v1.append(a2[v6] - a2[v5])
            while v2 and a2[v2[-1][1]] <= a2[v4]:
                v5, v6 = v2.pop()
                v1.append(a2[v6] - a2[v3])
                v3 = v5
            v2.append((v3, v4))
        while v2:
            v5, v6 = v2.pop()
            v1.append(a2[v6] - a2[v5])
        if a1 > len(v1):
            a1 = len(v1)
        else:
            nth_element(v1, a1 - 1, compare=lambda a, b: a > b)
        return sum((v1[i] for v8 in range(a1)))
