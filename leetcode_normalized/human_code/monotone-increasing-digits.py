class C1(object):

    def monotoneIncreasingDigits(self, a1):
        """
        """
        v1 = list(map(int, list(str(a1))))
        v2 = len(v1)
        for v3 in reversed(range(1, len(v1))):
            if v1[v3 - 1] > v1[v3]:
                v2 = v3
                v1[v3 - 1] -= 1
        for v3 in range(v2, len(v1)):
            v1[v3] = 9
        return int(''.join(map(str, v1)))
