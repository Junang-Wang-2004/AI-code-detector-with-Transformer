import collections

class C1(object):

    def findMatrix(self, a1):
        """
        """
        v1 = []
        v2 = collections.Counter()
        for v3 in a1:
            if v2[v3] == len(v1):
                v1.append([])
            v1[v2[v3]].append(v3)
            v2[v3] += 1
        return v1
