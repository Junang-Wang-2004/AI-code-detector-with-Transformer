import itertools

class C1(object):

    def areAlmostEqual(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3 in zip(a1, a2):
            if v2 == v3:
                continue
            if len(v1) == 2:
                return False
            v1.append([v2, v3] if not v1 else [v3, v2])
        return not v1 or (len(v1) == 2 and v1[0] == v1[1])
