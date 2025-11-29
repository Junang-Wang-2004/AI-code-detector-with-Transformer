from collections import defaultdict

class C1:

    def countOfAtoms(self, a1):
        v1 = [defaultdict(int)]
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = a1[v2]
            if v4.isupper():
                v5 = v4
                v2 += 1
                while v2 < v3 and a1[v2].islower():
                    v5 += a1[v2]
                    v2 += 1
                v6 = 0
                while v2 < v3 and a1[v2].isdigit():
                    v6 = v6 * 10 + int(a1[v2])
                    v2 += 1
                v1[-1][v5] += v6 if v6 else 1
            elif v4 == '(':
                v1.append(defaultdict(int))
                v2 += 1
            elif v4 == ')':
                v2 += 1
                v7 = 0
                while v2 < v3 and a1[v2].isdigit():
                    v7 = v7 * 10 + int(a1[v2])
                    v2 += 1
                v8 = v1.pop()
                v9 = v7 if v7 else 1
                for v10, v11 in v8.items():
                    v1[-1][v10] += v11 * v9
            else:
                v2 += 1
        v12 = v1[0]
        v13 = sorted(v12)
        v14 = []
        for v10 in v13:
            v11 = v12[v10]
            v14.append(v10 + str(v11) if v11 > 1 else v10)
        return ''.join(v14)
