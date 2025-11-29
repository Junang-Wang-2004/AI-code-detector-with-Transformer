class C1:

    def removeComments(self, a1):
        v1 = []
        v2 = False
        for v3 in a1:
            v4 = []
            v5 = 0
            v6 = len(v3)
            while v5 < v6:
                if v2:
                    if v5 + 1 < v6 and v3[v5:v5 + 2] == '*/':
                        v2 = False
                        v5 += 2
                    else:
                        v5 += 1
                    continue
                if v5 + 1 < v6 and v3[v5:v5 + 2] == '//':
                    break
                if v5 + 1 < v6 and v3[v5:v5 + 2] == '/*':
                    v2 = True
                    v5 += 2
                    continue
                v4.append(v3[v5])
                v5 += 1
            if v4:
                v1.append(''.join(v4))
        return v1
