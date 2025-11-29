class Solution:
    def evaluateExpression(self, expression):
        OPS = {
            "add": int.__add__,
            "sub": int.__sub__,
            "mul": int.__mul__,
            "div": int.__floordiv__
        }

        def evaluate(idx):
            start = idx
            while idx < len(expression) and expression[idx].isdigit():
                idx += 1
            if idx > start:
                return int(expression[start:idx]), idx

            start = idx
            while idx < len(expression) and expression[idx].isalpha():
                idx += 1
            op = OPS[expression[start:idx]]

            idx += 1  # '('
            lhs, idx = evaluate(idx)
            idx += 1  # ','
            rhs, idx = evaluate(idx)
            idx += 1  # ')'

            return op(lhs, rhs), idx

        return evaluate(0)[0]
