class C1(object):

    def corpFlightBookings(self, a1, a2):
        """
        """
        v1 = [0] * (a2 + 1)
        for v2, v3, v4 in a1:
            v1[v2 - 1] += v4
            v1[v3] -= v4
        for v2 in range(1, len(v1)):
            v1[v2] += v1[v2 - 1]
        v1.pop()
        return v1
