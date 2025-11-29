class C1(object):

    def scoreOfStudents(self, a1, a2):
        """
        """
        v1 = 1000

        def evaluate(a1):

            def compute(a1, a2):
                v1, v2 = (a1.pop(), a1.pop())
                a1.append(ops[a2.pop()](v2, v1))
            v1 = {'+': operator.add, '*': operator.mul}
            v2 = {'+': 0, '*': 1}
            v3, v4, v5 = ([], [], 0)
            for v6 in a1:
                if v6.isdigit():
                    v3.append(int(v6))
                else:
                    while v4 and v2[v4[-1]] >= v2[v6]:
                        compute(v3, v4)
                    v4.append(v6)
            while v4:
                compute(v3, v4)
            return v3[-1]
        v2 = (len(a1) + 1) // 2
        v3 = [[set() for v4 in range(v2)] for v4 in range(v2)]
        for v5 in range(v2):
            v3[v5][v5].add(int(a1[v5 * 2]))
        for v6 in range(1, v2):
            for v7 in range(v2 - v6):
                v8 = v7 + v6
                for v9 in range(v7, v8):
                    if a1[2 * v9 + 1] == '+':
                        v3[v7][v8].update((x + y for v10 in v3[v7][v9] for v11 in v3[v9 + 1][v8] if v10 + v11 <= v1))
                    else:
                        v3[v7][v8].update((v10 * v11 for v10 in v3[v7][v9] for v11 in v3[v9 + 1][v8] if v10 * v11 <= v1))
        v12 = evaluate(a1)
        return sum((5 if ans == v12 else 2 if ans in v3[0][-1] else 0 for v13 in a2))
