class C1(object):

    def isValidSerialization(self, a1):
        """
        """

        def split_iter(a1, a2):
            v1 = 0
            for v2 in range(len(a1)):
                if a1[v2] == a2:
                    yield a1[v1:v2]
                    v1 = v2 + 1
            yield a1[v1:]
        if not a1:
            return False
        v1, v2 = (0, a1.count(',') + 1)
        for v3 in split_iter(a1, ','):
            v2 -= 1
            if v3 == '#':
                v1 -= 1
                if v1 < 0:
                    break
            else:
                v1 += 1
        return v2 == 0 and v1 < 0
