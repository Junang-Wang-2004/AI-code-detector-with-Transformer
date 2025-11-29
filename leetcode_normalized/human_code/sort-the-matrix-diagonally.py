import collections

class C1(object):

    def diagonalSort(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in range(len(a1)):
            for v3 in range(len(a1[0])):
                v1[v2 - v3].append(a1[v2][v3])
        for v4 in v1.values():
            v4.sort()
        for v2 in reversed(range(len(a1))):
            for v3 in reversed(range(len(a1[0]))):
                a1[v2][v3] = v1[v2 - v3].pop()
        return a1
