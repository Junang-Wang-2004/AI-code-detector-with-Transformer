class C1(object):

    def matchPlayersAndTrainers(self, a1, a2):
        a1.sort()
        a2.sort()
        v1, v2 = (0, 0)
        v3 = 0
        v4, v5 = (len(a1), len(a2))
        while v1 < v4 and v2 < v5:
            if a1[v1] <= a2[v2]:
                v3 += 1
                v1 += 1
                v2 += 1
            else:
                v2 += 1
        return v3
