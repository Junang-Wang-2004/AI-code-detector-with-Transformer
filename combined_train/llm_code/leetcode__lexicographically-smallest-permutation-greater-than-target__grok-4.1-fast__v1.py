class C1(object):

    def lexGreaterPermutation(self, a1, a2):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = v1[:]
        v4 = len(a2)
        v5 = -1
        for v6 in range(v4):
            v7 = ord(a2[v6]) - ord('a')
            if v3[v7] == 0:
                break
            v8 = any((v3[k] > 0 for v9 in range(v7 + 1, 26)))
            if v8:
                v5 = v6
            v3[v7] -= 1
        if v5 == -1:
            return ''
        v10 = []
        for v6 in range(v5):
            v10.append(a2[v6])
            v1[ord(a2[v6]) - ord('a')] -= 1
        v11 = ord(a2[v5]) - ord('a')
        v12 = None
        for v9 in range(v11 + 1, 26):
            if v1[v9] > 0:
                v12 = chr(ord('a') + v9)
                break
        v10.append(v12)
        v1[ord(v12) - ord('a')] -= 1
        for v9 in range(26):
            v10.extend([chr(ord('a') + v9)] * v1[v9])
        return ''.join(v10)
