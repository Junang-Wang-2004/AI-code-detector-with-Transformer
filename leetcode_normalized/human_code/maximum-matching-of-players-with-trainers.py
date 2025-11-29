class C1(object):

    def matchPlayersAndTrainers(self, a1, a2):
        """
        """
        a1.sort()
        a2.sort()
        v1 = 0
        for v2 in a2:
            if a1[v1] > v2:
                continue
            v1 += 1
            if v1 == len(a1):
                break
        return v1
