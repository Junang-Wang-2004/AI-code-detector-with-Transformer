class C1(object):

    def firstDayBeenInAllRooms(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * len(a1)
        for v3 in range(1, len(v2)):
            v2[v3] = (v2[v3 - 1] + 1 + (v2[v3 - 1] - v2[a1[v3 - 1]]) + 1) % v1
        return v2[-1]
