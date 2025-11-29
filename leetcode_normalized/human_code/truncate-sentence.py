class C1(object):

    def truncateSentence(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            if a1[v1] == ' ':
                a2 -= 1
                if not a2:
                    return a1[:v1]
        return a1
