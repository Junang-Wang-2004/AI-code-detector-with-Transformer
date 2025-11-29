import itertools

class C1(object):

    def backspaceCompare(self, a1, a2):
        """
        """

        def findNextChar(a1):
            v1 = 0
            for v2 in reversed(range(len(a1))):
                if a1[v2] == '#':
                    v1 += 1
                elif v1:
                    v1 -= 1
                else:
                    yield a1[v2]
        return all((x == y for v1, v2 in itertools.zip_longest(findNextChar(a1), findNextChar(a2))))
