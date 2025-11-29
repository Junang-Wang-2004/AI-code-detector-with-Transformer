class C1:

    def originalDigits(self, a1):
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = [0] * 10
        v3[0] = v1[ord('z') - ord('a')]
        v3[2] = v1[ord('w') - ord('a')]
        v3[4] = v1[ord('u') - ord('a')]
        v3[6] = v1[ord('x') - ord('a')]
        v3[8] = v1[ord('g') - ord('a')]
        v3[1] = v1[ord('o') - ord('a')] - v3[0] - v3[2] - v3[4]
        v3[3] = v1[ord('t') - ord('a')] - v3[2]
        v3[5] = v1[ord('f') - ord('a')] - v3[4]
        v3[7] = v1[ord('s') - ord('a')] - v3[6]
        v3[9] = v1[ord('n') - ord('a')] - v3[1] - v3[7]
        v4 = []
        for v5 in range(10):
            v4.extend(str(v5) * v3[v5])
        return ''.join(v4)
