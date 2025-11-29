class C1(object):

    def toGoatLatin(self, a1):
        """
        """

        def convert(a1):
            v1 = set('aeiouAEIOU')
            for v2, v3 in enumerate(a1.split(), 1):
                if v3[0] not in v1:
                    v3 = v3[1:] + v3[:1]
                yield (v3 + 'ma' + 'a' * v2)
        return ' '.join(convert(a1))
