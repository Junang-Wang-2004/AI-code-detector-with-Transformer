import collections

class C1(object):

    def equalFrequency(self, a1):
        """
        """
        v1 = collections.Counter(collections.Counter(a1))
        for v2 in a1:
            v1[v2] -= 1
            if len(collections.Counter((v2 for v2 in v1.values() if v2))) == 1:
                return True
            v1[v2] += 1
        return False
