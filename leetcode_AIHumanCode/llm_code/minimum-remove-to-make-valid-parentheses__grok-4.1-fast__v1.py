class Solution:
    def minRemoveToMakeValid(self, s):
        stk = []
        to_skip = set()
        for idx, char in enumerate(s):
            if char == '(':
                stk.append(idx)
            elif char == ')':
                if stk:
                    stk.pop()
                else:
                    to_skip.add(idx)
        while stk:
            to_skip.add(stk.pop())
        output = []
        for idx, char in enumerate(s):
            if idx not in to_skip:
                output.append(char)
        return ''.join(output)
