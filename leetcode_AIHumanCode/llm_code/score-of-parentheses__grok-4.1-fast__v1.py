class Solution:
    def scoreOfParentheses(self, s):
        stk = []
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            else:
                opened = stk.pop()
                if i - opened == 1:
                    res += 1 << len(stk)
        return res
