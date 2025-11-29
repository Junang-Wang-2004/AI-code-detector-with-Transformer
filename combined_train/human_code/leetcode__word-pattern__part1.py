class C1(object):

    def wordPattern(self, a1, a2):
        """
        """
        if len(a1) != self.wordCount(a2):
            return False
        v1, v2 = ({}, {})
        for v3, v4 in zip(a1, self.wordGenerator(a2)):
            if v4 not in v1 and v3 not in v2:
                v1[v4] = v3
                v2[v3] = v4
            elif v4 not in v1 or v1[v4] != v3:
                return False
        return True

    def wordCount(self, a1):
        v1 = 1 if a1 else 0
        for v2 in a1:
            if v2 == ' ':
                v1 += 1
        return v1

    def wordGenerator(self, a1):
        v1 = ''
        for v2 in a1:
            if v2 == ' ':
                yield v1
                v1 = ''
            else:
                v1 += v2
        yield v1
