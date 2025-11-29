class C1(object):

    def isCircularSentence(self, a1):
        """
        """
        return a1[0] == a1[-1] and all((a1[i - 1] == a1[i + 1] for v1 in range(len(a1)) if a1[v1] == ' '))
