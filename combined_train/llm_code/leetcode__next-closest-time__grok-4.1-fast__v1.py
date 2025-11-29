class C1:

    def nextClosestTime(self, a1):
        v1 = set(a1.replace(':', ''))
        v2, v3 = map(int, a1.split(':'))
        v4 = v2 * 60 + v3
        v5 = ''
        v6 = float('inf')
        for v7 in v1:
            for v8 in v1:
                v9 = int(v7 + v8)
                if not 0 <= v9 <= 23:
                    continue
                for v10 in v1:
                    for v11 in v1:
                        v12 = int(v10 + v11)
                        if not 0 <= v12 <= 59:
                            continue
                        v13 = v9 * 60 + v12
                        v14 = v13 - v4 if v13 > v4 else 1440 - v4 + v13
                        if v14 < v6:
                            v6 = v14
                            v5 = f'{v7}{v8}:{v10}{v11}'
        return v5
