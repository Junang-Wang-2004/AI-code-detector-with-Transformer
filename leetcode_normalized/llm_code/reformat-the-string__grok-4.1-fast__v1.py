class C1:

    def reformat(self, a1):
        v1 = [ch for v2 in a1 if v2.isalpha()]
        v3 = [v2 for v2 in a1 if v2.isdigit()]
        v4 = len(v1)
        v5 = len(v3)
        if abs(v4 - v5) > 1:
            return ''
        v6 = []
        v7 = v8 = 0
        if v4 >= v5:
            for v9 in range(v5):
                v6.append(v1[v7])
                v7 += 1
                v6.append(v3[v8])
                v8 += 1
            if v7 < v4:
                v6.append(v1[v7])
        else:
            for v9 in range(v4):
                v6.append(v3[v8])
                v8 += 1
                v6.append(v1[v7])
                v7 += 1
            if v8 < v5:
                v6.append(v3[v8])
        return ''.join(v6)
