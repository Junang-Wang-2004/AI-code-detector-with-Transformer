class C1(object):

    def numberOfSpecialChars(self, a1):
        v1 = len(a1)
        v2 = [-1] * 26
        v3 = [v1] * 26
        for v4, v5 in enumerate(a1):
            v6 = ord(v5.lower()) - ord('a')
            if v5.islower():
                v2[v6] = v4
            elif v5.isupper():
                v3[v6] = min(v3[v6], v4)
        v7 = 0
        for v8 in range(26):
            if v2[v8] >= 0 and v3[v8] < v1 and (v2[v8] < v3[v8]):
                v7 += 1
        return v7
