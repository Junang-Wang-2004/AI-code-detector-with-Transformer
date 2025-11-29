import itertools

class C1(object):

    def dietPlanPerformance(self, a1, a2, a3, a4):
        """
        """
        v1 = sum(itertools.islice(a1, 0, a2))
        v2 = int(v1 > a4) - int(v1 < a3)
        for v3 in range(a2, len(a1)):
            v1 += a1[v3] - a1[v3 - a2]
            v2 += int(v1 > a4) - int(v1 < a3)
        return v2
