class C1(object):

    def numberOfAlternatingGroups(self, a1):
        """
        """
        return sum((a1[i] != a1[(i + 1) % len(a1)] != a1[(i + 2) % len(a1)] for v1 in range(len(a1))))
