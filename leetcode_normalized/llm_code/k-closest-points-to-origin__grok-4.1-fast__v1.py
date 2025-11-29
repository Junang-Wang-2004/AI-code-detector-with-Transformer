import random

class C1:

    def kClosest(self, a1, a2):
        random.shuffle(a1)

        def squared_distance(a1):
            return a1[0] * a1[0] + a1[1] * a1[1]

        def partition(a1, a2):
            v1 = squared_distance(a1[a2])
            v2 = a1
            for v3 in range(a1, a2):
                if squared_distance(a1[v3]) < v1:
                    a1[v2], a1[v3] = (a1[v3], a1[v2])
                    v2 += 1
            a1[v2], a1[a2] = (a1[a2], a1[v2])
            return v2

        def select(a1, a2, a3):
            if a1 >= a2:
                return
            v1 = partition(a1, a2)
            if v1 == a3:
                return
            elif v1 > a3:
                select(a1, v1 - 1, a3)
            else:
                select(v1 + 1, a2, a3)
        select(0, len(a1) - 1, a2 - 1)
        return a1[:a2]
