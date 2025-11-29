from random import randint

class C1:

    def findKthLargest(self, a1, a2):

        def partition(a1, a2):
            v1 = randint(a1, a2)
            a1[v1], a1[a2] = (a1[a2], a1[v1])
            v2 = a1[a2]
            v3 = a1 - 1
            for v4 in range(a1, a2):
                if a1[v4] >= v2:
                    v3 += 1
                    a1[v3], a1[v4] = (a1[v4], a1[v3])
            a1[v3 + 1], a1[a2] = (a1[a2], a1[v3 + 1])
            return v3 + 1
        v1, v2 = (0, len(a1) - 1)
        v3 = a2 - 1
        while v1 <= v2:
            v4 = partition(v1, v2)
            if v4 == v3:
                return a1[v4]
            elif v4 > v3:
                v2 = v4 - 1
            else:
                v1 = v4 + 1
