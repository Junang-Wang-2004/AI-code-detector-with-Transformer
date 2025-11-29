class C1(object):

    def findDisappearedNumbers(self, a1):
        """
        """
        for v1 in range(len(a1)):
            if a1[abs(a1[v1]) - 1] > 0:
                a1[abs(a1[v1]) - 1] *= -1
        v2 = []
        for v1 in range(len(a1)):
            if a1[v1] > 0:
                v2.append(v1 + 1)
            else:
                a1[v1] *= -1
        return v2

    def findDisappearedNumbers2(self, a1):
        """
        """
        return list(set(range(1, len(a1) + 1)) - set(a1))

    def findDisappearedNumbers3(self, a1):
        for v1 in range(len(a1)):
            v2 = abs(a1[v1]) - 1
            a1[v2] = -abs(a1[v2])
        return [v1 + 1 for v1 in range(len(a1)) if a1[v1] > 0]
