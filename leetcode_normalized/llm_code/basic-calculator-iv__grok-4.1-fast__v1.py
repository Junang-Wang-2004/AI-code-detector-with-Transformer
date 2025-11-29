class C1:

    def __init__(self, a1=None):
        self.terms = {}
        if a1 is None:
            return
        if a1.isdigit():
            self.terms[()] = int(a1)
        else:
            self.terms[a1,] = 1

    def _prune(self):
        v1 = [k for v2, v3 in self.terms.items() if v3 == 0]
        for v2 in v1:
            del self.terms[v2]

    def __add__(self, a1):
        v1 = C1()
        for v2, v3 in self.terms.items():
            v1.terms[v2] = v1.terms.get(v2, 0) + v3
        for v2, v3 in a1.terms.items():
            v1.terms[v2] = v1.terms.get(v2, 0) + v3
        v1._prune()
        return v1

    def __sub__(self, a1):
        v1 = C1()
        for v2, v3 in self.terms.items():
            v1.terms[v2] = v1.terms.get(v2, 0) + v3
        for v2, v3 in a1.terms.items():
            v1.terms[v2] = v1.terms.get(v2, 0) - v3
        v1._prune()
        return v1

    def __mul__(self, a1):
        v1 = C1()
        for v2, v3 in self.terms.items():
            for v4, v5 in a1.terms.items():
                v6 = tuple(sorted(set(v2) | set(v4)))
                v1.terms[v6] = v1.terms.get(v6, 0) + v3 * v5
        v1._prune()
        return v1

    def substitute(self, a1):
        v1 = C1()
        for v2, v3 in self.terms.items():
            v4 = v3
            v5 = []
            for v6 in v2:
                if v6 in a1:
                    v4 *= a1[v6]
                else:
                    v5.append(v6)
            v7 = tuple(v5) if v5 else ()
            v1.terms[v7] = v1.terms.get(v7, 0) + v4
        v1._prune()
        return v1

    def format_terms(self):
        v1 = sorted(self.terms.items(), key=lambda kv: (-len(kv[0]), kv[0]))
        return ['*'.join((str(kv[1]),) + kv[0]) for v2 in v1]

class C2:

    def basicCalculatorIV(self, a1, a2, a3):
        v1 = dict(zip(a2, a3))
        v2 = self._shunt_parse(a1)
        v3 = v2.substitute(v1)
        return v3.format_terms()

    def _shunt_parse(self, a1):
        v1 = []
        v2 = []
        v3 = 0
        while v3 < len(a1):
            v4 = a1[v3]
            if v4.isalnum():
                v5 = ''
                while v3 < len(a1) and a1[v3].isalnum():
                    v5 += a1[v3]
                    v3 += 1
                v2.append(C1(v5))
                continue
            if v4 == '(':
                v1.append(v4)
            elif v4 == ')':
                while v1[-1] != '(':
                    self._reduce(v2, v1)
                v1.pop()
            elif v4 in '+-*':
                v6 = 1 if v4 in '+-' else 2
                while v1 and v1[-1] != '(':
                    v7 = 1 if v1[-1] in '+-' else 2
                    if v7 < v6:
                        break
                    self._reduce(v2, v1)
                v1.append(v4)
            v3 += 1
        while v1:
            self._reduce(v2, v1)
        return v2[0]

    def _reduce(self, a1, a2):
        v1 = a1.pop()
        v2 = a1.pop()
        v3 = a2.pop()
        if v3 == '+':
            a1.append(v2 + v1)
        elif v3 == '-':
            a1.append(v2 - v1)
        elif v3 == '*':
            a1.append(v2 * v1)
