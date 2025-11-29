class C1(object):

    def lexPalindromicPermutation(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        if sum((c % 2 for v3 in v1)) > 1:
            return ''
        v2 = -1
        if len(a2) % 2:
            v2 = next((v2 for v2, v3 in enumerate(v1) if v3 % 2))
            v1[v2] -= 1
        v4 = []
        for v5 in range(len(a2) // 2):
            v1[ord(a2[v5]) - ord('a')] -= 2
            v4.append(a2[v5])
            if v1[ord(a2[v5]) - ord('a')] < 0:
                break
        else:
            if len(a2) % 2:
                v4.append(chr(ord('a') + v2))
            v6 = ''.join(v4)
            v6 += v6[:len(a2) // 2][::-1]
            if v6 > a2:
                return v6
            if len(a2) % 2:
                v4.pop()
        while v4:
            v3 = ord(v4.pop()) - ord('a')
            v1[v3] += 2
            for v5 in range(v3 + 1, len(v1)):
                if not v1[v5]:
                    continue
                v1[v5] -= 2
                v4.append(chr(ord('a') + v5))
                for v7 in range(len(v1)):
                    if not v1[v7]:
                        continue
                    while v1[v7]:
                        v1[v7] -= 2
                        v4.append(chr(ord('a') + v7))
                if len(a2) % 2:
                    v4.append(chr(ord('a') + v2))
                v6 = ''.join(v4)
                v6 += v6[:len(a2) // 2][::-1]
                return v6
        return ''
