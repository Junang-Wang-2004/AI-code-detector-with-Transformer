class C1:

    def smallestNumber(self, a1):
        if a1 == 0:
            return 0
        v1 = str(abs(a1))
        v2 = a1 > 0
        v3 = list(v1)
        v4 = v3.count('0')
        v5 = [d for v6 in v3 if v6 != '0']
        if v2:
            v5.sort()
            v7 = v5[0]
            v8 = ['0'] * v4 + v5[1:]
        else:
            v5.sort(reverse=True)
            v7 = v5[0]
            v8 = v5[1:] + ['0'] * v4
        v9 = v7 + ''.join(v8)
        return (1 if v2 else -1) * int(v9)
