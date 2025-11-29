import random
import collections

class C1(object):

    def findMaximumElegance(self, a1, a2):
        """
        """

        def nth_element(a1, a2, a3=0, a4=lambda a, b: a < b):

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
            v1 = len(a1) - 1
            while a3 <= v1:
                v2 = random.randint(a3, v1)
                v3, v4 = tri_partition(a1, a3, v1, a1[v2], a4)
                if v3 <= a2 <= v4:
                    return
                elif v3 > a2:
                    v1 = v3 - 1
                else:
                    a3 = v4 + 1

        def nlargest(a1, a2):
            nth_element(a2, a1 - 1, compare=lambda a, b: a > b)
            return sorted(a2[:a1], reverse=True)
        v1 = 0
        v2 = set()
        v3 = []
        for v4, v5 in nlargest(a2, a1):
            if v5 in v2:
                v3.append(v4)
            v1 += v4
            v2.add(v5)
        v6 = collections.defaultdict(int)
        for v4, v5 in a1:
            if v5 in v2:
                continue
            v6[v5] = max(v6[v5], v4)
        v7 = len(v2)
        v8 = v1 + v7 ** 2
        for v4 in nlargest(min(len(v3), len(v6)), list(v6.values())):
            v1 += v4 - v3.pop()
            v7 += 1
            v8 = max(v8, v1 + v7 ** 2)
        return v8
