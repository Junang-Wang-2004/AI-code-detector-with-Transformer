class Solution(object):
    def calculate(self, s):
        def expr(pos):
            res = term(pos)
            while pos[0] < len(s) and s[pos[0]] in '+-':
                op = s[pos[0]]
                pos[0] += 1
                t = term(pos)
                res += t if op == '+' else res - t
            return res

        def term(pos):
            res = factor(pos)
            while pos[0] < len(s) and s[pos[0]] in '*/':
                op = s[pos[0]]
                pos[0] += 1
                f = factor(pos)
                res = res * f if op == '*' else int(res / f)
            return res

        def factor(pos):
            if s[pos[0]].isdigit():
                num = 0
                while pos[0] < len(s) and s[pos[0]].isdigit():
                    num = num * 10 + int(s[pos[0]])
                    pos[0] += 1
                return num
            pos[0] += 1
            res = expr(pos)
            pos[0] += 1
            return res

        pos = [0]
        return expr(pos)
