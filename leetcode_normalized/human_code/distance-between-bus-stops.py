import itertools

class C1(object):

    def distanceBetweenBusStops(self, a1, a2, a3):
        """
        """
        if a2 > a3:
            a2, a3 = (a3, a2)
        v3 = sum(itertools.islice(a1, a2, a3))
        v4 = sum(itertools.islice(a1, 0, a2)) + sum(itertools.islice(a1, a3, len(a1)))
        return min(v3, v4)
