import collections

class C1(object):

    def repairCars(self, a1, a2):
        """
        """

        def check(a1):
            return sum((int((a1 // k) ** 0.5) * v for v1, v2 in cnt.items())) >= a2
        v1 = collections.Counter(a1)
        v2, v3 = (1, min(v1.keys()) * a2 ** 2)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2
