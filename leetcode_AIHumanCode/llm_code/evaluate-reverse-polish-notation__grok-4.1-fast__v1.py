class Solution:
    def evalRPN(self, tokens):
        stk = []
        for t in tokens:
            try:
                stk.append(int(t))
            except ValueError:
                rhs = stk.pop()
                lhs = stk.pop()
                if t == '+':
                    stk.append(lhs + rhs)
                elif t == '-':
                    stk.append(lhs - rhs)
                elif t == '*':
                    stk.append(lhs * rhs)
                else:
                    stk.append(int(lhs / rhs))
        return stk.pop()
