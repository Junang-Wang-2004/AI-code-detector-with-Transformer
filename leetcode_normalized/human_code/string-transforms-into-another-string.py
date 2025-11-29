import itertools

class C1(object):

    def canConvert(self, a1, a2):
        """
        """
        if a1 == a2:
            return True
        v1 = {}
        for v2, v3 in zip(a1, a2):
            if v1.setdefault(v2, v3) != v3:
                return False
        return len(set(a2)) < 26
