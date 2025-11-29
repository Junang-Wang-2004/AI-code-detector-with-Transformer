class C1(object):

    def maximumTop(self, a1, a2):
        """
        """
        if len(a1) == 1 == a2 % 2:
            return -1
        if a2 <= 1:
            return a1[a2]
        return max((a1[i] for v1 in range(min(a2 + 1, len(a1))) if v1 != a2 - 1))
