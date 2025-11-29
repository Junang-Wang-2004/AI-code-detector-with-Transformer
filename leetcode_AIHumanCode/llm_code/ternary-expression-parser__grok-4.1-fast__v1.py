class Solution:
    def parseTernary(self, expression):
        if not expression:
            return ""

        def helper(pos):
            ch = expression[pos]
            pos += 1
            if pos < len(expression) and expression[pos] == '?':
                pos += 1
                true_part, pos = helper(pos)
                pos += 1
                false_part, pos = helper(pos)
                return (true_part if ch == 'T' else false_part), pos
            return ch, pos

        result, _ = helper(0)
        return result
