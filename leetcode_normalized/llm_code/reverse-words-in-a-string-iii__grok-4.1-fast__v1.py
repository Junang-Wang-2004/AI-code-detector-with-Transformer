class C1:

    def reverseWords(self, a1):
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2] == ' ':
                v1.append(' ')
                v2 += 1
                continue
            v4 = v2
            while v4 < v3 and a1[v4] != ' ':
                v4 += 1
            for v5 in range(v4 - 1, v2 - 1, -1):
                v1.append(a1[v5])
            v2 = v4
        return ''.join(v1)
