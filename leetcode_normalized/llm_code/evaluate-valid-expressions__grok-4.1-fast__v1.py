class C1:

    def evaluateExpression(self, a1):
        v1 = {'add': int.__add__, 'sub': int.__sub__, 'mul': int.__mul__, 'div': int.__floordiv__}

        def evaluate(a1):
            v1 = a1
            while a1 < len(a1) and a1[a1].isdigit():
                a1 += 1
            if a1 > v1:
                return (int(a1[v1:a1]), a1)
            v1 = a1
            while a1 < len(a1) and a1[a1].isalpha():
                a1 += 1
            v3 = v1[a1[v1:a1]]
            a1 += 1
            v4, a1 = evaluate(a1)
            a1 += 1
            v5, a1 = evaluate(a1)
            a1 += 1
            return (v3(v4, v5), a1)
        return evaluate(0)[0]
