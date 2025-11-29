# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def reverseParentheses(self, s):
        """
        """
        stk = [[]]
        for c in s:
            if c == '(':
                stk.append([])
            elif c == ')':
                end = stk.pop()
                end.reverse()
                stk[-1].extend(end)
            else:
                stk[-1].append(c)
        return "".join(stk.pop())
