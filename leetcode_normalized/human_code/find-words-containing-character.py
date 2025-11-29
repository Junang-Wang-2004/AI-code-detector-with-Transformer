class C1(object):

    def findWordsContaining(self, a1, a2):
        """
        """
        return [i for v1, v2 in enumerate(a1) if a2 in v2]
