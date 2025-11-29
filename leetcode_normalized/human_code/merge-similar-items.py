class C1(object):

    def mergeSimilarItems(self, a1, a2):
        """
        """
        return sorted((Counter(dict(a1)) + Counter(dict(a2))).items())
