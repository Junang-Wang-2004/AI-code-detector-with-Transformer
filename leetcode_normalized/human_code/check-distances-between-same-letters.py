class C1(object):

    def checkDistances(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            if v1 + a2[ord(a1[v1]) - ord('a')] + 1 >= len(a1) or a1[v1 + a2[ord(a1[v1]) - ord('a')] + 1] != a1[v1]:
                return False
            a2[ord(a1[v1]) - ord('a')] = -1
        return True
