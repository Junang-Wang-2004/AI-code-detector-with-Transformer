class Solution(object):
    def minOperationsToFlip(self, expression):
        def parse_primary(p):
            if expression[p].isdigit():
                c = expression[p]
                tf = int(c != '0')
                tt = int(c != '1')
                return [tf, tt], p + 1
            p += 1
            res, p = parse_expression(p)
            p += 1
            return res, p

        def parse_expression(p):
            res, p = parse_primary(p)
            while p < len(expression) and expression[p] in '&|':
                op = expression[p]
                p += 1
                right, p = parse_primary(p)
                l_false, l_true = res
                r_false, r_true = right
                if op == '&':
                    new_false = min(l_false, r_false)
                    new_true = min(l_true + r_true, 1 + min(l_true, r_true))
                else:
                    new_false = min(l_false + r_false, 1 + min(l_false, r_false))
                    new_true = min(l_true, r_true)
                res = [new_false, new_true]
            return res, p

        costs, _ = parse_expression(0)
        return max(costs)
