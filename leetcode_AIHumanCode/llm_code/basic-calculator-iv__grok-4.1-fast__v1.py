class Polynomial:
    def __init__(self, token=None):
        self.terms = {}
        if token is None:
            return
        if token.isdigit():
            self.terms[()] = int(token)
        else:
            self.terms[(token,)] = 1

    def _prune(self):
        to_delete = [k for k, c in self.terms.items() if c == 0]
        for k in to_delete:
            del self.terms[k]

    def __add__(self, rhs):
        res = Polynomial()
        for m, c in self.terms.items():
            res.terms[m] = res.terms.get(m, 0) + c
        for m, c in rhs.terms.items():
            res.terms[m] = res.terms.get(m, 0) + c
        res._prune()
        return res

    def __sub__(self, rhs):
        res = Polynomial()
        for m, c in self.terms.items():
            res.terms[m] = res.terms.get(m, 0) + c
        for m, c in rhs.terms.items():
            res.terms[m] = res.terms.get(m, 0) - c
        res._prune()
        return res

    def __mul__(self, rhs):
        res = Polynomial()
        for m1, c1 in self.terms.items():
            for m2, c2 in rhs.terms.items():
                new_m = tuple(sorted(set(m1) | set(m2)))
                res.terms[new_m] = res.terms.get(new_m, 0) + c1 * c2
        res._prune()
        return res

    def substitute(self, vals):
        res = Polynomial()
        for m, c in self.terms.items():
            coef = c
            rem_vars = []
            for v in m:
                if v in vals:
                    coef *= vals[v]
                else:
                    rem_vars.append(v)
            new_m = tuple(rem_vars) if rem_vars else ()
            res.terms[new_m] = res.terms.get(new_m, 0) + coef
        res._prune()
        return res

    def format_terms(self):
        sorted_items = sorted(self.terms.items(), key=lambda kv: (-len(kv[0]), kv[0]))
        return ["*".join((str(kv[1]),) + kv[0]) for kv in sorted_items]


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        valmap = dict(zip(evalvars, evalints))
        root_poly = self._shunt_parse(expression)
        reduced = root_poly.substitute(valmap)
        return reduced.format_terms()

    def _shunt_parse(self, s):
        ops = []
        vals = []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch.isalnum():
                tkn = ''
                while idx < len(s) and s[idx].isalnum():
                    tkn += s[idx]
                    idx += 1
                vals.append(Polynomial(tkn))
                continue
            if ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops[-1] != '(':
                    self._reduce(vals, ops)
                ops.pop()
            elif ch in '+-*':
                p_ch = 1 if ch in '+-' else 2
                while ops and ops[-1] != '(':
                    p_top = 1 if ops[-1] in '+-' else 2
                    if p_top < p_ch:
                        break
                    self._reduce(vals, ops)
                ops.append(ch)
            idx += 1
        while ops:
            self._reduce(vals, ops)
        return vals[0]

    def _reduce(self, vals, ops):
        rgt = vals.pop()
        lft = vals.pop()
        opc = ops.pop()
        if opc == '+':
            vals.append(lft + rgt)
        elif opc == '-':
            vals.append(lft - rgt)
        elif opc == '*':
            vals.append(lft * rgt)
