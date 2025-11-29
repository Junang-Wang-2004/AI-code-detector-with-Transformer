class Solution:
    def solveEquation(self, equation):
        parts = equation.split('=')
        lhs, rhs = parts[0], parts[1]

        def extract(s):
            cx, cn = 0, 0
            pos = 0
            length = len(s)
            while pos < length:
                multiplier = 1
                if s[pos] in '+-':
                    multiplier = 1 if s[pos] == '+' else -1
                    pos += 1
                digits = 0
                saw_digits = False
                while pos < length and s[pos].isdigit():
                    saw_digits = True
                    digits = digits * 10 + int(s[pos])
                    pos += 1
                if pos < length and s[pos] == 'x':
                    pos += 1
                    cx += multiplier * (digits if saw_digits else 1)
                elif saw_digits:
                    cn += multiplier * digits
            return cx, cn

        clx, cln = extract(lhs)
        crx, crn = extract(rhs)
        coeff = clx - crx
        const = cln - crn
        if coeff != 0:
            val = -const // coeff
            return f'x={val}'
        return 'Infinite solutions' if const == 0 else 'No solution'
