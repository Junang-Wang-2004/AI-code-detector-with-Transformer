from random import randint

class C1(object):

    def topKFrequent(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = []
        for v3, v4 in v1.items():
            v2.append((-v4, v3))
        self.kthElement(v2, a2 - 1)
        v5 = []
        for v6 in range(a2):
            v5.append(v2[v6][1])
        return v5

    def kthElement(self, a1, a2):

        def PartitionAroundPivot(a1, a2, a3, a4):
            v1 = a4[a3]
            v2 = a1
            a4[a3], a4[a2] = (a4[a2], a4[a3])
            for v3 in range(a1, a2):
                if a4[v3] < v1:
                    a4[v3], a4[v2] = (a4[v2], a4[v3])
                    v2 += 1
            a4[a2], a4[v2] = (a4[v2], a4[a2])
            return v2
        v1, v2 = (0, len(a1) - 1)
        while v1 <= v2:
            v3 = randint(v1, v2)
            v4 = PartitionAroundPivot(v1, v2, v3, a1)
            if v4 == a2:
                return
            elif v4 > a2:
                v2 = v4 - 1
            else:
                v1 = v4 + 1
