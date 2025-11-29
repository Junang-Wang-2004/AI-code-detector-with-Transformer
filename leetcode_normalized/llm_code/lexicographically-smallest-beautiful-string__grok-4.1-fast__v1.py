class C1(object):

    def smallestBeautifulString(self, a1, a2):
        v1 = len(a1)
        v2 = [ord(c) - ord('a') for v3 in a1]
        for v4 in range(v1 - 1, -1, -1):
            v5 = v2[v4 - 1] if v4 >= 1 else -1
            v6 = v2[v4 - 2] if v4 >= 2 else -1
            v7 = v2[v4] + 1
            while v7 < a2 and (v7 == v5 or v7 == v6):
                v7 += 1
            if v7 < a2:
                v8 = v2[:v4] + [v7]
                for v9 in range(v4 + 1, v1):
                    v10 = v8[v9 - 1]
                    v11 = v8[v9 - 2] if v9 >= 2 else -1
                    v12 = 0
                    while v12 == v10 or v12 == v11:
                        v12 += 1
                    v8.append(v12)
                return ''.join((chr(ord('a') + x) for v13 in v8))
        return ''
