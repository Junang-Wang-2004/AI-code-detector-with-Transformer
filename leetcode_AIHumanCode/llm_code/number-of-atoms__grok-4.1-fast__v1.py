from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        counts = [defaultdict(int)]
        idx = 0
        length = len(formula)
        while idx < length:
            ch = formula[idx]
            if ch.isupper():
                elem = ch
                idx += 1
                while idx < length and formula[idx].islower():
                    elem += formula[idx]
                    idx += 1
                multiplicity = 0
                while idx < length and formula[idx].isdigit():
                    multiplicity = multiplicity * 10 + int(formula[idx])
                    idx += 1
                counts[-1][elem] += multiplicity if multiplicity else 1
            elif ch == '(':
                counts.append(defaultdict(int))
                idx += 1
            elif ch == ')':
                idx += 1
                multiplier = 0
                while idx < length and formula[idx].isdigit():
                    multiplier = multiplier * 10 + int(formula[idx])
                    idx += 1
                prev = counts.pop()
                factor = multiplier if multiplier else 1
                for sym, qty in prev.items():
                    counts[-1][sym] += qty * factor
            else:
                idx += 1
        final = counts[0]
        symbols = sorted(final)
        parts = []
        for sym in symbols:
            qty = final[sym]
            parts.append(sym + str(qty) if qty > 1 else sym)
        return ''.join(parts)
