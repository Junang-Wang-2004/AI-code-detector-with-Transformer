class C1:

    def repeatLimitedString(self, a1, a2):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = []
        v4 = -1
        v5 = 0
        while True:
            v6 = False
            for v7 in range(25, -1, -1):
                if v1[v7] > 0 and (v7 != v4 or v5 < a2):
                    v3.append(chr(v7 + ord('a')))
                    v1[v7] -= 1
                    if v7 == v4:
                        v5 += 1
                    else:
                        v4 = v7
                        v5 = 1
                    v6 = True
                    break
            if not v6:
                break
        return ''.join(v3)
