class C1:

    def ambiguousCoordinates(self, a1):
        v1 = a1[1:-1]
        v2 = len(v1)
        v3 = []
        for v4 in range(1, v2):
            v5 = v4
            for v6 in range(1, v5 + 1):
                v7 = v1[:v6]
                v8 = v1[v6:v4]
                if len(v7) > 1 and v7[0] == '0':
                    continue
                if v8 and v8[-1] == '0':
                    continue
                v9 = v7 + ('.' + v8 if v8 else '')
                v10 = v4
                v11 = v2 - v10
                for v12 in range(1, v11 + 1):
                    v13 = v1[v10:v10 + v12]
                    v14 = v1[v10 + v12:]
                    if len(v13) > 1 and v13[0] == '0':
                        continue
                    if v14 and v14[-1] == '0':
                        continue
                    v15 = v13 + ('.' + v14 if v14 else '')
                    v3.append('({}, {})'.format(v9, v15))
        return v3
