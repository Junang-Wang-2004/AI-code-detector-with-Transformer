class C1(object):

    def lengthLongestPath(self, a1):
        """
        """

        def split_iter(a1, a2):
            v1 = 0
            for v2 in range(len(a1)):
                if a1[v2] == a2:
                    yield a1[v1:v2]
                    v1 = v2 + 1
            yield a1[v1:]
        v1 = 0
        v2 = {0: 0}
        for v3 in split_iter(a1, '\n'):
            v4 = v3.lstrip('\t')
            v5 = len(v3) - len(v4)
            if '.' in v4:
                v1 = max(v1, v2[v5] + len(v4))
            else:
                v2[v5 + 1] = v2[v5] + len(v4) + 1
        return v1
