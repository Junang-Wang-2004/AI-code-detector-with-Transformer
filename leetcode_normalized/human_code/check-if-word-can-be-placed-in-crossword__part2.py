class C1(object):

    def placeWordInCrossword(self, a1, a2):
        """
        """
        v1 = [a2, a2[::-1]]
        for v2 in (a1, list(zip(*a1))):
            for v3 in v2:
                v4 = ''.join(v3).split('#')
                for v5 in v4:
                    if len(v5) != len(a2):
                        continue
                    for v6 in v1:
                        if all((v5[i] in (v6[i], ' ') for v7 in range(len(v5)))):
                            return True
        return False
