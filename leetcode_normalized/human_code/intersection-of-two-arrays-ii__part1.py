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
        if len(a1) > len(a2):
            return self.intersect(a2, a1)

        def binary_search(a1, a2, a3, a4, a5):
            while a3 < a4:
                v1 = a3 + (a4 - a3) / 2
                if a1(a2[v1], a5):
                    a4 = v1
                else:
                    a3 = v1 + 1
            return a3
        (a1.sort(), a2.sort())
        v1 = []
        v2 = 0
        for v3 in a1:
            v2 = binary_search(lambda x, y: x >= y, a2, v2, len(a2), v3)
            if v2 != len(a2) and a2[v2] == v3:
                v1 += (v3,)
                v2 += 1
        return v1
