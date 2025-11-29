class C1(object):

    def catchMaximumAmountofPeople(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if not a1[v3]:
                continue
            while v2 < v3 - a2:
                v2 += 1
            while v2 <= min(v3 + a2, len(a1) - 1):
                if a1[v2] == 0:
                    break
                v2 += 1
            if v2 <= min(v3 + a2, len(a1) - 1):
                v1 += 1
                v2 += 1
        return v1
