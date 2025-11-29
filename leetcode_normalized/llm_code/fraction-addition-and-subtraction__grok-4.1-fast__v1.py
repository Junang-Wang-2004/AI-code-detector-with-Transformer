class C1(object):

    def fractionAddition(self, a1):

        def greatest_common_divisor(a1, a2):
            a1 = abs(a1)
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = a1
        v2 = 0
        v3 = len(v1)
        v4 = []
        v5 = []
        while v2 < v3:
            v6 = 1
            if v1[v2] == '+':
                v2 += 1
            elif v1[v2] == '-':
                v6 = -1
                v2 += 1
            v7 = v2
            while v2 < v3 and v1[v2].isdigit():
                v2 += 1
            v8 = int(v1[v7:v2]) * v6
            if v2 < v3 and v1[v2] == '/':
                v2 += 1
            v9 = v2
            while v2 < v3 and v1[v2].isdigit():
                v2 += 1
            v10 = int(v1[v9:v2])
            v4.append(v8)
            v5.append(v10)
        v11 = 0
        v12 = 1
        for v13 in range(len(v4)):
            v14 = v4[v13]
            v15 = v5[v13]
            v11 = v11 * v15 + v14 * v12
            v12 = v12 * v15
            v16 = greatest_common_divisor(v11, v12)
            v11 //= v16
            v12 //= v16
        return f'{v11}/{v12}'
