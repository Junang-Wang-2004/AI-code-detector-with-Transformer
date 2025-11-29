class C1(object):

    def smallestNumber(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1) + 1):
            if not (v2 == len(a1) or a1[v2] == 'I'):
                continue
            for v3 in reversed(list(range(len(v1) + 1, v2 + 1 + 1))):
                v1.append(v3)
        return ''.join(map(str, v1))
