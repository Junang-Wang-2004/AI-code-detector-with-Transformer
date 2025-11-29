class C1(object):

    def reverseOnlyLetters(self, a1):
        """
        """

        def getNext(a1):
            for v1 in reversed(range(len(a1))):
                if a1[v1].isalpha():
                    yield a1[v1]
        v1 = []
        v2 = getNext(a1)
        for v3 in range(len(a1)):
            if a1[v3].isalpha():
                v1.append(next(v2))
            else:
                v1.append(a1[v3])
        return ''.join(v1)
