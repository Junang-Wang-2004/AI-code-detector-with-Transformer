class C1:

    def makeLargestSpecial(self, a1: str) -> str:

        def process(a1: str) -> str:
            v1 = []
            v2 = 0
            v3 = len(a1)
            while v2 < v3:
                v4 = 0
                v5 = v2
                while v2 < v3:
                    v4 += 1 if a1[v2] == '1' else -1
                    v2 += 1
                    if v4 == 0:
                        break
                v6 = process(a1[v5 + 1:v2 - 1])
                v1.append('1' + v6 + '0')
            v1.sort(reverse=True)
            return ''.join(v1)
        return process(a1)
