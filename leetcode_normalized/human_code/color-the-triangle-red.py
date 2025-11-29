class C1(object):

    def colorRed(self, a1):
        """
        """
        v1 = [[1, 1]]
        for v2 in range(2, a1 + 1):
            if v2 % 2 == a1 % 2:
                v1.extend(([v2, j] for v3 in range(1 if v2 % 4 == a1 % 4 else 3, 2 * v2, 2)))
            else:
                v1.append([v2, 2 if v2 % 4 == (a1 - 1) % 4 else 1])
        return v1
