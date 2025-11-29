class C1(object):

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
