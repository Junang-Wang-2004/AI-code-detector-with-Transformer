class C1(object):

    def countVowels(self, a1):
        """
        """
        v1 = set('aeiou')
        return sum(((i - 0 + 1) * (len(a1) - 1 - i + 1) for v2, v3 in enumerate(a1) if v3 in v1))
