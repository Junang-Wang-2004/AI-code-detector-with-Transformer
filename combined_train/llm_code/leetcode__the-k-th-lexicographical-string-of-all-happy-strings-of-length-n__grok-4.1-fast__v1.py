class C1:

    def getHappyString(self, a1, a2):
        if a1 == 0:
            return ''
        v1 = []
        v2 = None
        for v3 in range(a1):
            v4 = 1 << a1 - 1 - v3
            v5 = False
            for v6 in 'abc':
                if v6 == v2:
                    continue
                if a2 <= v4:
                    v1.append(v6)
                    v2 = v6
                    v5 = True
                    break
                a2 -= v4
            if not v5:
                return ''
        return ''.join(v1)
