class Solution(object):
    def reverseParentheses(self, s):
        buf = []
        for ch in s:
            if ch == ')':
                temp = []
                while buf and buf[-1] != '(':
                    temp.append(buf.pop())
                buf.pop()
                buf.extend(temp)
            else:
                buf.append(ch)
        return ''.join(buf)
