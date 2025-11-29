class Solution:
    def isValid(self, s):
        stk = []
        for c in s:
            if c == 'c':
                if not stk or stk.pop() != 'b':
                    return False
                if not stk or stk.pop() != 'a':
                    return False
            else:
                stk.append(c)
        return not stk
