class Solution:
    def calculate(self, s):
        pos = [0]

        def skip_spaces():
            while pos[0] < len(s) and s[pos[0]].isspace():
                pos[0] += 1

        def parse_number():
            skip_spaces()
            num = 0
            while pos[0] < len(s) and s[pos[0]].isdigit():
                num = num * 10 + int(s[pos[0]])
                pos[0] += 1
            return num

        def parse_factor():
            skip_spaces()
            if pos[0] < len(s) and s[pos[0]] == '(':
                pos[0] += 1
                result = parse_expression()
                pos[0] += 1
                skip_spaces()
                return result
            return parse_number()

        def parse_term():
            result = parse_factor()
            skip_spaces()
            while pos[0] < len(s) and s[pos[0]] in '*/':
                oper = s[pos[0]]
                pos[0] += 1
                factor_val = parse_factor()
                skip_spaces()
                if oper == '*':
                    result *= factor_val
                else:
                    result = int(result / factor_val)
            return result

        def parse_expression():
            result = parse_term()
            skip_spaces()
            while pos[0] < len(s) and s[pos[0]] in '+-':
                oper = s[pos[0]]
                pos[0] += 1
                term_val = parse_term()
                skip_spaces()
                if oper == '+':
                    result += term_val
                else:
                    result -= term_val
            return result

        ans = parse_expression()
        skip_spaces()
        return ans
