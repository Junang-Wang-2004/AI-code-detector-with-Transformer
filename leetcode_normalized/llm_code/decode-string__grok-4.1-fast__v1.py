class C1:

    def decodeString(self, a1):
        v1 = []
        v2 = 0
        v3 = ''
        for v4 in a1:
            if v4.isdigit():
                v2 = v2 * 10 + int(v4)
            elif v4 == '[':
                v1.append(v3)
                v1.append(v2)
                v3 = ''
                v2 = 0
            elif v4 == ']':
                v5 = v1.pop()
                v6 = v1.pop()
                v3 = v6 + v3 * v5
            else:
                v3 += v4
        return v3
