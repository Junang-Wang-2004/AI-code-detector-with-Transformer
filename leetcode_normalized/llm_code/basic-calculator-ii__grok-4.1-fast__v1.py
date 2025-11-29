class C1:

    def calculate(self, a1):
        v1 = [0]

        def skip_spaces():
            while v1[0] < len(a1) and a1[v1[0]].isspace():
                v1[0] += 1

        def parse_number():
            skip_spaces()
            v1 = 0
            while v1[0] < len(a1) and a1[v1[0]].isdigit():
                v1 = v1 * 10 + int(a1[v1[0]])
                v1[0] += 1
            return v1

        def parse_factor():
            skip_spaces()
            if v1[0] < len(a1) and a1[v1[0]] == '(':
                v1[0] += 1
                v1 = parse_expression()
                v1[0] += 1
                skip_spaces()
                return v1
            return parse_number()

        def parse_term():
            v1 = parse_factor()
            skip_spaces()
            while v1[0] < len(a1) and a1[v1[0]] in '*/':
                v2 = a1[v1[0]]
                v1[0] += 1
                v3 = parse_factor()
                skip_spaces()
                if v2 == '*':
                    v1 *= v3
                else:
                    v1 = int(v1 / v3)
            return v1

        def parse_expression():
            v1 = parse_term()
            skip_spaces()
            while v1[0] < len(a1) and a1[v1[0]] in '+-':
                v2 = a1[v1[0]]
                v1[0] += 1
                v3 = parse_term()
                skip_spaces()
                if v2 == '+':
                    v1 += v3
                else:
                    v1 -= v3
            return v1
        v2 = parse_expression()
        skip_spaces()
        return v2
