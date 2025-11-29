import collections

class C1(object):

    def intersect(self, a1, a2):
        """
        """
        if len(a1) > len(a2):
            return self.intersect(a2, a1)
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        v3 = []
        for v2 in a2:
            if v1[v2] > 0:
                v3 += (v2,)
                v1[v2] -= 1
        return v3

    def intersect2(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1) & collections.Counter(a2)
        v2 = []
        for v3 in v1:
            v2.extend([v3] * v1[v3])
        return v2

class C1(object):

    def intersect(self, a1, a2):
        """
        """
        (a1.sort(), a2.sort())
        v1 = []
        v2, v3 = (0, 0)
        while v2 < len(a1) and v3 < len(a2):
            if a1[v2] < a2[v3]:
                v2 += 1
            elif a1[v2] > a2[v3]:
                v3 += 1
            else:
                v1 += (a1[v2],)
                v2 += 1
                v3 += 1
        return v1
