class C1(object):

    def validStrings(self, a1):
        """
        """
        v1 = [[]]
        for v2 in range(a1):
            v3 = []
            for v4 in v1:
                if not v4 or v4[-1] == '1':
                    v3.append(v4 + ['0'])
                v3.append(v4 + ['1'])
            v1 = v3
        return [''.join(v4) for v4 in v1]
