class C1(object):

    def removeDuplicateLetters(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = []
        v4 = [False] * 26
        for v2 in a1:
            v5 = ord(v2) - ord('a')
            v1[v5] -= 1
            if not v4[v5]:
                while v3 and ord(v3[-1]) > ord(v2) and (v1[ord(v3[-1]) - ord('a')] > 0):
                    v4[ord(v3.pop()) - ord('a')] = False
                v3.append(v2)
                v4[v5] = True
        return ''.join(v3)
