import bisect

class C1(object):

    def countRectangles(self, a1, a2):
        """
        """
        v1 = max((y for v2, v3 in a1))
        v4 = [[] for v2 in range(v1 + 1)]
        for v5, v3 in a1:
            v4[v3].append(v5)
        for v6 in v4:
            v6.sort()
        return [sum((len(v4[v3]) - bisect.bisect_left(v4[v3], v5) for v3 in range(v3, v1 + 1))) for v5, v3 in a2]
