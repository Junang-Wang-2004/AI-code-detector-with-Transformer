class C1(object):

    def minCharacters(self, a1, a2):
        v1 = [0] * 26
        v2 = [0] * 26
        v3 = ord('a')
        for v4 in a1:
            v1[ord(v4) - v3] += 1
        for v4 in a2:
            v2[ord(v4) - v3] += 1
        v5 = max((v1[i] + v2[i] for v6 in range(26)))
        v7 = len(a1) + len(a2) - v5
        v8 = [0] * 27
        v9 = [0] * 27
        for v6 in range(26):
            v8[v6 + 1] = v8[v6] + v1[v6]
            v9[v6 + 1] = v9[v6] + v2[v6]
        v10, v11 = (len(a1), len(a2))
        for v6 in range(25):
            v12 = v8[v6 + 1]
            v13 = v9[v6 + 1]
            v7 = min(v7, v10 - v12 + v13, v11 - v13 + v12)
        return v7
