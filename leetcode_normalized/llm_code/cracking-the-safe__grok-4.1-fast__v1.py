class C1:

    def crackSafe(self, a1: int, a2: int) -> str:
        v1 = a2 ** a1
        v2 = set()
        v3 = [str(a2 - 1)] * (a1 - 1)
        while len(v2) < v1:
            v4 = ''.join(v3[-(a1 - 1):])
            for v5 in range(a2):
                v6 = v4 + str(v5)
                if v6 not in v2:
                    v2.add(v6)
                    v3.append(str(v5))
                    break
        return ''.join(v3)
