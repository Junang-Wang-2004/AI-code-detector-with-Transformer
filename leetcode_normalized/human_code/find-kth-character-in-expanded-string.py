class C1(object):

    def kthCharacter(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] == ' ':
                v1 = 0
                a2 -= 1
            else:
                v1 += 1
                a2 -= v1
            if a2 < 0:
                break
        return a1[v2]
