class C1(object):

    def countCharacters(self, a1, a2):
        v1 = ord('a')
        v2 = [0] * 26
        for v3 in a2:
            v2[ord(v3) - v1] += 1
        v4 = 0
        for v5 in a1:
            v6 = [0] * 26
            for v3 in v5:
                v6[ord(v3) - v1] += 1
            if all((v6[k] <= v2[k] for v7 in range(26))):
                v4 += len(v5)
        return v4
