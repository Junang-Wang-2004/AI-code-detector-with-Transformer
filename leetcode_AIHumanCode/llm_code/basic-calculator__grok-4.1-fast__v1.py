class Solution:
    def calculate(self, s):
        pos = [0]
        def factor():
            if s[pos[0]].isdigit():
                num = 0
                while pos[0] < len(s) and s[pos[0]].isdigit():
                    num = num * 10 + int(s[pos[0]])
                    pos[0] += 1
                return num
            pos[0] += 1
            res = expr()
            pos[0] += 1
            return res

        def term():
            res = factor()
            while pos[0] < len(s) and s[pos[0]] in '*/':
                sign = s[pos[0]]
                pos[0] += 1
                f = factor()
                if sign == '*':
                    res *= f
                else:
                    res //= f
            return res

        def expr():
            res = term()
            while pos[0] < len(s) and s[pos[0]] in '+-':
                sign = s[pos[0]]
                pos[0] += 1
                t = term()
                if sign == '+':
                    res += t
                else:
                    res -= t
            return res

        return expr()
