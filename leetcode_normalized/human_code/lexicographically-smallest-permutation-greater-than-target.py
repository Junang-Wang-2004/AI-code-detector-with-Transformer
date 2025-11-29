class C1(object):

    def lexGreaterPermutation(self, a1, a2):
        """
        """

        def nxt(a1, a2):
            for v1 in range(ord(a2) - ord('a') + 1, len(a1)):
                if not a1[v1]:
                    continue
                return chr(ord('a') + v1)
            return ' '
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = v1[:]
        v4 = -1
        for v5, v2 in enumerate(a2):
            v6 = nxt(v3, v2)
            if v6 != ' ':
                v4 = v5
            if not v3[ord(v2) - ord('a')]:
                break
            v3[ord(v2) - ord('a')] -= 1
        if v4 == -1:
            return ''
        v7 = []
        for v5 in range(v4):
            v7.append(a2[v5])
            v1[ord(a2[v5]) - ord('a')] -= 1
        v6 = nxt(v1, a2[v4])
        v7.append(v6)
        v1[ord(v6) - ord('a')] -= 1
        for v5 in range(len(v1)):
            for v8 in range(v1[v5]):
                v7.append(chr(ord('a') + v5))
                v1[v5] -= 1
        return ''.join(v7)
