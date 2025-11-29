class C1:

    def smallestEquivalentString(self, a1, a2, a3):
        v1 = list(range(26))

        def root(a1):
            v1 = a1
            while v1[v1] != v1:
                v1 = v1[v1]
            v2 = a1
            while v2 != v1:
                v3, v2 = (v1[v2], v3)
                v1[v2] = v1
            return v1
        v2 = len(a1)
        v3 = ord('a')
        for v4 in range(v2):
            v5 = ord(a1[v4]) - v3
            v6 = ord(a2[v4]) - v3
            v7 = root(v5)
            v8 = root(v6)
            if v7 != v8:
                if v7 < v8:
                    v1[v8] = v7
                else:
                    v1[v7] = v8
        v9 = []
        for v10 in a3:
            v9.append(chr(root(ord(v10) - v3) + v3))
        return ''.join(v9)
