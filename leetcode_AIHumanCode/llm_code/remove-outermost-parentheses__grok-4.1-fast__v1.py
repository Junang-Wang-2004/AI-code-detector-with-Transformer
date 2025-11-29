class Solution:
    def removeOuterParentheses(self, S):
        res = []
        level = 0
        for ch in S:
            if ch == '(':
                level += 1
                if level > 1:
                    res.append(ch)
            else:
                if level > 1:
                    res.append(ch)
                level -= 1
        return ''.join(res)
