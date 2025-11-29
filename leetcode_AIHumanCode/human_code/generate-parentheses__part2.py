# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
# recursive solution
class Solution2(object):
    def generateParenthesis(self, n):
        """
        """
        def generateParenthesisRecu(left, right, curr, result):
            if left == 0 and right == 0:
                result.append("".join(curr))
            if left > 0:
                curr.append('(')
                generateParenthesisRecu(left-1, right, curr, result)
                curr.pop()
            if left < right:
                curr.append(')')
                generateParenthesisRecu(left, right-1, curr, result)
                curr.pop()

        result = []
        generateParenthesisRecu(n, n, [], result)
        return result
