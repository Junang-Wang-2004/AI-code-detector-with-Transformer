class Solution:
    def parseBoolExpr(self, expr):
        def evaluate(idx):
            ch = expr[idx]
            if ch == 't':
                return True, idx + 1
            if ch == 'f':
                return False, idx + 1
            op = ch
            idx += 2
            args = []
            while expr[idx] != ')':
                if expr[idx] == ',':
                    idx += 1
                    continue
                val, idx = evaluate(idx)
                args.append(val)
            idx += 1
            if op == '&':
                return all(args), idx
            if op == '|':
                return any(args), idx
            return not args[0], idx

        return evaluate(0)[0]
