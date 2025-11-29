import itertools

class C1(object):

    def restoreString(self, a1, a2):
        """
        """
        v1 = [''] * len(a1)
        for v2, v3 in zip(a2, a1):
            v1[v2] = v3
        return ''.join(v1)
