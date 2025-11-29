class C1(object):

    def pushDominoes(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] == 'R':
                v2 = len(a1)
            elif a1[v3] == 'L':
                v2 = 0
            else:
                v2 = max(v2 - 1, 0)
            v1[v3] += v2
        v2 = 0
        for v3 in reversed(range(len(a1))):
            if a1[v3] == 'L':
                v2 = len(a1)
            elif a1[v3] == 'R':
                v2 = 0
            else:
                v2 = max(v2 - 1, 0)
            v1[v3] -= v2
        return ''.join(('.' if v2 == 0 else 'R' if v2 > 0 else 'L' for v2 in v1))
