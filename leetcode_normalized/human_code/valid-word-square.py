class C1(object):

    def validWordSquare(self, a1):
        """
        """
        for v1 in range(len(a1)):
            for v2 in range(len(a1[v1])):
                if v2 >= len(a1) or v1 >= len(a1[v2]) or a1[v2][v1] != a1[v1][v2]:
                    return False
        return True
