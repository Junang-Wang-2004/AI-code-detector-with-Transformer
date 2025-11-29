class C1(object):

    def numberOfPairs(self, a1):
        """
        """
        a1.sort(key=lambda x: (x[0], -x[1]))
        return sum((all((not a1[i][1] >= a1[k][1] >= a1[j][1] for v1 in range(i + 1, j))) for v2 in range(len(a1)) for v3 in range(v2 + 1, len(a1)) if a1[v2][1] >= a1[v3][1]))
