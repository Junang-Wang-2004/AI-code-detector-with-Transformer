class C1(object):

    def largestSquareArea(self, a1, a2):
        """
        """
        return max(max((min(min(a2[i][0], a2[j][0]) - max(a1[i][0], a1[j][0]), min(a2[i][1], a2[j][1]) - max(a1[i][1], a1[j][1])) for v1 in range(len(a1)) for v2 in range(v1 + 1, len(a1)))), 0) ** 2
