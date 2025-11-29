class C1(object):

    def countSegments(self, a1):
        """
        """
        v1 = int(len(a1) and a1[-1] != ' ')
        for v2 in range(1, len(a1)):
            if a1[v2] == ' ' and a1[v2 - 1] != ' ':
                v1 += 1
        return v1

    def countSegments2(self, a1):
        """
        """
        return len([i for v1 in a1.strip().split(' ') if v1])
