class C1:

    def decodeCiphertext(self, a1, a2):
        v1 = len(a1)
        if a2 == 0:
            return ''
        v2 = v1 // a2
        v3 = []
        v4 = v2 + 1
        for v5 in range(v2):
            v6 = v5
            while v6 < v1:
                v3.append(a1[v6])
                v6 += v4
        while v3 and v3[-1] == ' ':
            v3.pop()
        return ''.join(v3)
