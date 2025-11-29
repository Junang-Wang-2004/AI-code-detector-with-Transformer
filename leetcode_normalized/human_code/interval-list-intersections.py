class C1(object):

    def __init__(self, a1=0, a2=0):
        self.start = a1
        self.end = a2

class C2(object):

    def intervalIntersection(self, a1, a2):
        """
        """
        v1 = []
        v2, v3 = (0, 0)
        while v2 < len(a1) and v3 < len(a2):
            v4 = max(a1[v2].start, a2[v3].start)
            v5 = min(a1[v2].end, a2[v3].end)
            if v4 <= v5:
                v1.append(C1(v4, v5))
            if a1[v2].end < a2[v3].end:
                v2 += 1
            else:
                v3 += 1
        return v1
