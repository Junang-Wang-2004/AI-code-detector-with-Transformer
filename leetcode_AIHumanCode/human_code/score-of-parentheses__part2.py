# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def scoreOfParentheses(self, S):
        """
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(1, 2*last)
        return stack[0]

