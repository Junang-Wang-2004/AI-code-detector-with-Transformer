import collections

class C1(object):

    def judgeCircle(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return v1['L'] == v1['R'] and v1['U'] == v1['D']
