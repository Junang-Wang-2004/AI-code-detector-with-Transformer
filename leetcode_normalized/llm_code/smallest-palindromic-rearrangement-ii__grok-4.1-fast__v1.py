class C1:

    def smallestPalindrome(self, a1, a2):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = [0] * 26
        for v4 in a1[:v2]:
            v3[ord(v4) - 97] += 1
        v5 = 0
        v6 = 1
        v7 = -1
        v8 = 0
        for v9 in range(25, -1, -1):
            for v10 in range(1, v3[v9] + 1):
                v5 += 1
                v6 = v6 * v5 // v10
                if v6 >= a2:
                    v7 = v9
                    v8 = v3[v9] - v10
                    break
            if v7 != -1:
                break
        if v7 == -1:
            return ''
        v11 = []
        for v12 in range(v7 + 1):
            v13 = v8 if v12 == v7 else v3[v12]
            v14 = chr(97 + v12)
            v11 += [v14] * v13
            v3[v12] -= v13
        while v5 > 0:
            for v12 in range(v7, 26):
                if v3[v12] == 0:
                    continue
                v15 = v6 * v3[v12] // v5
                if v15 < a2:
                    a2 -= v15
                    continue
                v6 = v15
                v3[v12] -= 1
                v5 -= 1
                v11.append(chr(97 + v12))
                break
        if v1 % 2:
            v11.append(a1[v2])
        return ''.join(v11 + v11[:v2][::-1])
