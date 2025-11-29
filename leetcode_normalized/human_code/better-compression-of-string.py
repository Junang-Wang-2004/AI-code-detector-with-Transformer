class C1(object):

    def betterCompression(self, a1):
        """
        """
        v1 = [0] * 26
        v2, v3 = (-1, 0)
        for v4 in range(len(a1)):
            if not a1[v4].isdigit():
                v2 = ord(a1[v4]) - ord('a')
                continue
            v3 = v3 * 10 + int(a1[v4])
            if v4 + 1 == len(a1) or not a1[v4 + 1].isdigit():
                v1[v2] += v3
                v3 = 0
        return ''.join(('%s%s' % (chr(ord('a') + v4), v2) for v4, v2 in enumerate(v1) if v2))
