from random import randint

class C1(object):

    def minTotalDistance(self, a1):
        """
        """
        v1 = [i for v2, v3 in enumerate(a1) for v4 in v3 if v4 == 1]
        v5 = [j for v3 in a1 for v6, v4 in enumerate(v3) if v4 == 1]
        v7 = self.findKthLargest(v1, len(v1) / 2 + 1)
        v8 = self.findKthLargest(v5, len(v5) / 2 + 1)
        return sum([abs(v7 - v2) + abs(v8 - v6) for v2, v3 in enumerate(a1) for v6, v4 in enumerate(v3) if v4 == 1])

    def findKthLargest(self, a1, a2):
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = randint(v1, v2)
            v4 = self.PartitionAroundPivot(v1, v2, v3, a1)
            if v4 == a2 - 1:
                return a1[v4]
            elif v4 > a2 - 1:
                v2 = v4 - 1
            else:
                v1 = v4 + 1

    def PartitionAroundPivot(self, a1, a2, a3, a4):
        v1 = a4[a3]
        v2 = a1
        a4[a3], a4[a2] = (a4[a2], a4[a3])
        for v3 in range(a1, a2):
            if a4[v3] > v1:
                a4[v3], a4[v2] = (a4[v2], a4[v3])
                v2 += 1
        a4[a2], a4[v2] = (a4[v2], a4[a2])
        return v2
