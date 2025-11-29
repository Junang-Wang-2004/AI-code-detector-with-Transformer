class Solution(object):
    def resultingString(self, s):
        stack = []
        for c in s:
            if stack and (abs(ord(c) - ord(stack[-1])) == 1 or abs(ord(c) - ord(stack[-1])) == 25):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
