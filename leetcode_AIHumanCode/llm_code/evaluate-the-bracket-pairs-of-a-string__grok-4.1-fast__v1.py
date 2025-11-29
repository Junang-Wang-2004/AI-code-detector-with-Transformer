class Solution:
    def evaluate(self, s, knowledge):
        mapping = dict(knowledge)
        parts = []
        pos = 0
        length = len(s)
        while pos < length:
            if s[pos] == '(':
                end = pos + 1
                while s[end] != ')':
                    end += 1
                variable = s[pos + 1:end]
                parts.append(mapping.get(variable, '?'))
                pos = end + 1
            else:
                parts.append(s[pos])
                pos += 1
        return ''.join(parts)
