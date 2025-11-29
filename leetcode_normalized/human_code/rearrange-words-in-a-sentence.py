class C1(object):

    def arrangeWords(self, a1):
        """
        """
        v1 = a1.split()
        v1[0] = v1[0].lower()
        v1.sort(key=len)
        v1[0] = v1[0].title()
        return ' '.join(v1)
