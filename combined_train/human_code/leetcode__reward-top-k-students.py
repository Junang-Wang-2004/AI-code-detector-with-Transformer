import random
import itertools

class C1(object):

    def topStudents(self, a1, a2, a3, a4, a5):
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
        v1, v2 = (set(a1), set(a2))
        v3 = []
        for v4, v5 in zip(a4, a3):
            v6 = sum((3 if w in v1 else -1 if w in v2 else 0 for v7 in v5.split()))
            v3.append((-v6, v4))
        nth_element(v3, a5 - 1)
        return [v4 for v8, v4 in sorted(v3[:a5])]
