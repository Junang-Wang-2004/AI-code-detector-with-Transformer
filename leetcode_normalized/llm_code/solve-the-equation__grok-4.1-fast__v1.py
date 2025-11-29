class C1:

    def solveEquation(self, a1):
        v1 = a1.split('=')
        v2, v3 = (v1[0], v1[1])

        def extract(a1):
            v1, v2 = (0, 0)
            v3 = 0
            v4 = len(a1)
            while v3 < v4:
                v5 = 1
                if a1[v3] in '+-':
                    v5 = 1 if a1[v3] == '+' else -1
                    v3 += 1
                v6 = 0
                v7 = False
                while v3 < v4 and a1[v3].isdigit():
                    v7 = True
                    v6 = v6 * 10 + int(a1[v3])
                    v3 += 1
                if v3 < v4 and a1[v3] == 'x':
                    v3 += 1
                    v1 += v5 * (v6 if v7 else 1)
                elif v7:
                    v2 += v5 * v6
            return (v1, v2)
        v4, v5 = extract(v2)
        v6, v7 = extract(v3)
        v8 = v4 - v6
        v9 = v5 - v7
        if v8 != 0:
            v10 = -v9 // v8
            return f'x={v10}'
        return 'Infinite solutions' if v9 == 0 else 'No solution'
