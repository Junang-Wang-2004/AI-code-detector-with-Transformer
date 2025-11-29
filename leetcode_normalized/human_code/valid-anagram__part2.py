class C1(object):

    def isAnagram(self, a1, a2):
        """
        """
        return collections.Counter(a1) == collections.Counter(a2)
