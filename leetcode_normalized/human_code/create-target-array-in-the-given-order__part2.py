import itertools

class C1(object):

    def createTargetArray(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3 in zip(a2, a1):
            v1.insert(v2, v3)
        return v1
