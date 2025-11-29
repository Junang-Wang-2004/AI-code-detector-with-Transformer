class C1:

    def removeSubstring(self, a1, a2):
        v1 = []
        v2 = [0]
        v3 = 2 * a2
        for v4 in a1:
            v1.append(v4)
            if v4 == '(':
                if v2[0] < a2:
                    v2[0] += 1
                elif v2[0] > a2:
                    v2[0] = 1
            elif v2[0] >= a2:
                v2[0] += 1
            else:
                v2[0] = 0
            if v2[0] == v3:
                for v5 in range(v3):
                    v1.pop()
                v2[0] = 0
                v6 = max(0, len(v1) - v3 + 1)
                for v7 in range(v6, len(v1)):
                    v8 = v1[v7]
                    if v8 == '(':
                        if v2[0] < a2:
                            v2[0] += 1
                        elif v2[0] > a2:
                            v2[0] = 1
                    elif v2[0] >= a2:
                        v2[0] += 1
                    else:
                        v2[0] = 0
        return ''.join(v1)
