class C1(object):

    def freqAlphabets(self, a1):
        """
        """

        def alpha(a1):
            return chr(ord('a') + int(a1) - 1)
        v1 = 0
        v2 = []
        while v1 < len(a1):
            if v1 + 2 < len(a1) and a1[v1 + 2] == '#':
                v2.append(alpha(a1[v1:v1 + 2]))
                v1 += 3
            else:
                v2.append(alpha(a1[v1]))
                v1 += 1
        return ''.join(v2)
