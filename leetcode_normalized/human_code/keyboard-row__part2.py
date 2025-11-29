class C1(object):

    def findWords(self, a1):
        """
        """
        v1 = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        v2 = []
        for v3 in a1:
            for v4 in v1:
                if all((letter in v4 for v5 in v3.lower())):
                    v2.append(v3)
        return v2
