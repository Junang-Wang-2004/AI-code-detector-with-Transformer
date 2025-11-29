class C1(object):

    def sortString(self, a1):
        """
        """
        v1, v2 = ([], [0] * 26)
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        while len(v1) != len(a1):
            for v3 in range(len(v2)):
                if not v2[v3]:
                    continue
                v1.append(chr(ord('a') + v3))
                v2[v3] -= 1
            for v3 in reversed(range(len(v2))):
                if not v2[v3]:
                    continue
                v1.append(chr(ord('a') + v3))
                v2[v3] -= 1
        return ''.join(v1)
