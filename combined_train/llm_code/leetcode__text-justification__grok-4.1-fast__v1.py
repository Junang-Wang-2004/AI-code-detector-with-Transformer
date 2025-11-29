class C1:

    def fullJustify(self, a1, a2):
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2 + 1
            v5 = len(a1[v2])
            while v4 < v3 and v5 + len(a1[v4]) + 1 <= a2:
                v5 += len(a1[v4]) + 1
                v4 += 1
            v6 = v4 - v2
            v7 = sum((len(w) for v8 in a1[v2:v4]))
            if v6 == 1 or v4 == v3:
                v9 = ' '.join(a1[v2:v4])
                v9 += ' ' * (a2 - len(v9))
            else:
                v10 = a2 - v7
                v11 = v10 // (v6 - 1)
                v12 = v10 % (v6 - 1)
                v13 = []
                for v14 in range(v6):
                    v13.append(a1[v2 + v14])
                    if v14 < v6 - 1:
                        v15 = v11 + (1 if v14 < v12 else 0)
                        v13.append(' ' * v15)
                v9 = ''.join(v13)
            v1.append(v9)
            v2 = v4
        return v1
