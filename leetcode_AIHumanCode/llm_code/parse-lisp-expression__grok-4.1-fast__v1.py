class Solution:
    def evaluate(self, expression):
        buf = ['']
        env = {}
        frames = []
        for ch in expression:
            if ch == '(':
                if buf[0] == 'let':
                    self._compute(buf, env)
                frames.append((buf[:], env.copy()))
                buf = ['']
            elif ch == ' ':
                buf.append('')
            elif ch == ')':
                val = self._compute(buf, env)
                buf, env = frames.pop()
                buf[-1] += val
            else:
                buf[-1] += ch
        return int(buf[0])

    def _compute(self, toks, scope):
        cmd = toks[0]
        if cmd in ('add', 'mult'):
            operands = [scope.get(term, term) for term in toks[1:]]
            x, y = map(int, operands)
            return str(x + y if cmd == 'add' else x * y)
        # let
        for k in range(1, len(toks) - 1, 2):
            key = toks[k]
            value = scope.get(toks[k + 1], toks[k + 1])
            scope[key] = value
        return scope.get(toks[-1], toks[-1])
