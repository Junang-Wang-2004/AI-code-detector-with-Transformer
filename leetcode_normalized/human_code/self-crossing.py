class C1(object):

    def isSelfCrossing(self, a1):
        """
        """
        if len(a1) >= 5 and a1[3] == a1[1] and (a1[4] + a1[0] >= a1[2]):
            return True
        for v1 in range(3, len(a1)):
            if a1[v1] >= a1[v1 - 2] and a1[v1 - 3] >= a1[v1 - 1]:
                return True
            elif v1 >= 5 and a1[v1 - 4] <= a1[v1 - 2] and (a1[v1] + a1[v1 - 4] >= a1[v1 - 2]) and (a1[v1 - 1] <= a1[v1 - 3]) and (a1[v1 - 5] + a1[v1 - 1] >= a1[v1 - 3]):
                return True
        return False
