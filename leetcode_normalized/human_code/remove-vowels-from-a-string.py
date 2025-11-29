class C1(object):

    def removeVowels(self, a1):
        """
        """
        v1 = set('aeiou')
        return ''.join((c for v2 in a1 if v2 not in v1))
