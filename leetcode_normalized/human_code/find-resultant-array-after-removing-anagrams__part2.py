import collections

class C1(object):

    def removeAnagrams(self, a1):
        """
        """
        v1 = []
        v2 = None
        for v3 in a1:
            v4 = sorted(v3)
            if v2 and v2 == v4:
                continue
            v2 = v4
            v1.append(v3)
        return v1
