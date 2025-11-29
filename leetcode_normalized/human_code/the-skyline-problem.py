v1, v2, v3 = (0, 1, 2)

class C1(object):

    def getSkyline(self, a1):
        v1 = self.ComputeSkylineInInterval(a1, 0, len(a1))
        v2 = []
        v3 = -1
        for v4 in v1:
            if v3 != -1 and v3 < v4[v1]:
                v2.append([v3, 0])
            v2.append([v4[v1], v4[v3]])
            v3 = v4[v2]
        if v3 != -1:
            v2.append([v3, 0])
        return v2

    def ComputeSkylineInInterval(self, a1, a2, a3):
        if a3 - a2 <= 1:
            return a1[a2:a3]
        v1 = a2 + (a3 - a2) / 2
        v2 = self.ComputeSkylineInInterval(a1, a2, v1)
        v3 = self.ComputeSkylineInInterval(a1, v1, a3)
        return self.MergeSkylines(v2, v3)

    def MergeSkylines(self, a1, a2):
        v1, v2 = (0, 0)
        v3 = []
        while v1 < len(a1) and v2 < len(a2):
            if a1[v1][v2] < a2[v2][v1]:
                v3.append(a1[v1])
                v1 += 1
            elif a2[v2][v2] < a1[v1][v1]:
                v3.append(a2[v2])
                v2 += 1
            elif a1[v1][v1] <= a2[v2][v1]:
                v1, v2 = self.MergeIntersectSkylines(v3, a1[v1], v1, a2[v2], v2)
            else:
                v2, v1 = self.MergeIntersectSkylines(v3, a2[v2], v2, a1[v1], v1)
        v3 += a1[v1:]
        v3 += a2[v2:]
        return v3

    def MergeIntersectSkylines(self, a1, a2, a3, a4, a5):
        if a2[v2] <= a4[v2]:
            if a2[v3] > a4[v3]:
                if a4[v2] != a2[v2]:
                    a4[v1] = a2[v2]
                    a1.append(a2)
                    a3 += 1
                else:
                    a5 += 1
            elif a2[v3] == a4[v3]:
                a4[v1] = a2[v1]
                a3 += 1
            else:
                if a2[v1] != a4[v1]:
                    a1.append([a2[v1], a4[v1], a2[v3]])
                a3 += 1
        elif a2[v3] >= a4[v3]:
            a5 += 1
        else:
            if a2[v1] != a4[v1]:
                a1.append([a2[v1], a4[v1], a2[v3]])
            a2[v1] = a4[v2]
            a1.append(a4)
            a5 += 1
        return (a3, a5)
