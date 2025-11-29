class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def expTree(self, s):
        precedence = {'+': 0, '-': 0, '*': 1, '/': 1}
        rpn = []
        ops = []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                rpn.append(str(num))
                continue
            if ch == '(':
                ops.append(ch)
            elif ch == ')':
                while ops and ops[-1] != '(':
                    rpn.append(ops.pop())
                ops.pop()
            elif ch in precedence:
                while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[ch]:
                    rpn.append(ops.pop())
                ops.append(ch)
            i += 1
        while ops:
            rpn.append(ops.pop())
        stack = []
        for tok in rpn:
            if tok.isdigit():
                stack.append(Node(tok))
            else:
                rgt = stack.pop()
                lft = stack.pop()
                stack.append(Node(tok, left=lft, right=rgt))
        return stack[0]
