class C1:

    def freqAlphabets(self, a1: str) -> str:
        v1 = []
        v2 = []
        for v3 in a1:
            if v3.isdigit():
                v1.append(v3)
            elif v3 == '#':
                v4 = v1.pop()
                v5 = v1.pop()
                v6 = int(v5 + v4)
                v2.append(chr(ord('a') + v6 - 1))
        while v1:
            v6 = int(v1.pop(0))
            v2.append(chr(ord('a') + v6 - 1))
        return ''.join(v2)
