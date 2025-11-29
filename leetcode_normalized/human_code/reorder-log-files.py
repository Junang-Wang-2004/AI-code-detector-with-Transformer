class C1(object):

    def reorderLogFiles(self, a1):
        """
        """

        def f(a1):
            v1, v2 = a1.split(' ', 1)
            return (0, v2, v1) if v2[0].isalpha() else (1,)
        a1.sort(key=f)
        return a1
