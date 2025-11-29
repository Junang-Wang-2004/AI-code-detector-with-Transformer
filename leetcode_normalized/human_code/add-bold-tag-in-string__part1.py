import collections
import functools

class C1(object):

    def addBoldTag(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        for v2 in a2:
            v3 = a1.find(v2)
            while v3 != -1:
                v1[v3:v3 + len(v2)] = [1] * len(v2)
                v3 = a1.find(v2, v3 + 1)
        v4 = []
        for v5 in range(len(a1)):
            if v1[v5] and (v5 == 0 or not v1[v5 - 1]):
                v4.append('<b>')
            v4.append(a1[v5])
            if v1[v5] and (v5 == len(a1) - 1 or not v1[v5 + 1]):
                v4.append('</b>')
        return ''.join(v4)
