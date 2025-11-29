import collections

class C1(object):

    def findSmallestInteger(self, a1, a2):
        """
        """
        v1 = collections.Counter((x % a2 for v2 in a1))
        for v3 in range(len(a1) + 1):
            if not v1[v3 % a2]:
                return v3
            v1[v3 % a2] -= 1
