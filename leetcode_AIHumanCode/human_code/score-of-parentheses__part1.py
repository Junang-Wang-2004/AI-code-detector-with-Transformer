# Time:  O(n)
# Space: O(1)


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        """
        result, depth = 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    result += 2**depth
        return result


