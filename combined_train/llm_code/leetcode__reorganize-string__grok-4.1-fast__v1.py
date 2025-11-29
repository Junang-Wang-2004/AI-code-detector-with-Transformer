class C1:

    def reorganizeString(self, a1):
        v1 = len(a1)
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        if max(v2) > (v1 + 1) // 2:
            return ''
        v4 = []
        v5 = None
        for v6 in range(v1):
            v7 = -1
            v8 = -1
            for v9 in range(26):
                v10 = chr(v9 + ord('a'))
                if v2[v9] > v7 and (v5 is None or v10 != v5):
                    v7 = v2[v9]
                    v8 = v9
            v3 = chr(v8 + ord('a'))
            v4.append(v3)
            v2[v8] -= 1
            v5 = v3
        return ''.join(v4)
