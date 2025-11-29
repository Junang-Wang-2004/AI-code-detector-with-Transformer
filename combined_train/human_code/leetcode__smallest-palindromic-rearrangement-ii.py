class C1(object):

    def smallestPalindrome(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in range(len(a1) // 2):
            v1[ord(a1[v2]) - ord('a')] += 1
        v3, v4, v5 = (0, 1, 0)
        for v2 in reversed(range(len(v1))):
            for v6 in range(1, v1[v2] + 1):
                v3 += 1
                v4 = v4 * v3 // v6
                if v4 >= a2:
                    v5 = v1[v2] - v6
                    break
            if v4 >= a2:
                break
        else:
            return ''
        v7 = []
        for v8 in range(v2 + 1):
            v9 = chr(ord('a') + v8)
            for v10 in range(v1[v8] if v8 != v2 else v5):
                v1[v8] -= 1
                v7.append(v9)
        while v3:
            for v8 in range(v2, len(v1)):
                if not v1[v8]:
                    continue
                v11 = v4 * v1[v8] // v3
                if v11 < a2:
                    a2 -= v11
                    continue
                v4 = v11
                v1[v8] -= 1
                v3 -= 1
                v7.append(chr(ord('a') + v8))
                break
        if len(a1) % 2:
            v7.append(a1[len(a1) // 2])
        v7.extend((v7[v2] for v2 in reversed(range(len(v7) - len(a1) % 2))))
        return ''.join(v7)
