import collections

class C1(object):

    def equalFrequency(self, a1):
        """
        """
        v1 = collections.Counter(iter(collections.Counter(a1).values()))
        if len(v1) > 2:
            return False
        if len(v1) == 1:
            v2 = list(v1.keys())[0]
            return v2 == 1 or v1[v2] == 1
        v2, v3 = list(v1.keys())
        if v2 > v3:
            v2, v3 = (v3, v2)
        return v2 == 1 and v1[v2] == 1 or (v2 + 1 == v3 and v1[v3] == 1)
