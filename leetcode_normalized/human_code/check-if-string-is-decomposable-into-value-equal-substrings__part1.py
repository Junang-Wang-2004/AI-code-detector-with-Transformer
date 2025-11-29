class C1(object):

    def isDecomposable(self, a1):
        """
        """
        if len(a1) % 3 != 2:
            return False
        for v1 in range(0, len(a1), 3):
            if any((a1[i] != a1[i - 1] for v2 in range(v1 + 1, min(v1 + 3, len(a1))))):
                break
        for v3 in reversed(range(v1 + 1, len(a1), 3)):
            if any((a1[v2] != a1[v2 + 1] for v2 in reversed(range(max(v3 - 2, v1), v3)))):
                break
        return v3 - v1 == 1
