class C1:

    def alphabetBoardPath(self, a1):
        v1 = []
        v2, v3 = (0, 0)
        for v4 in a1:
            v5 = (ord(v4) - 97) // 5
            v6 = (ord(v4) - 97) % 5
            while v2 > v5:
                v1.append('U')
                v2 -= 1
            while v3 > v6:
                v1.append('L')
                v3 -= 1
            while v3 < v6:
                v1.append('R')
                v3 += 1
            while v2 < v5:
                v1.append('D')
                v2 += 1
            v1.append('!')
        return ''.join(v1)
