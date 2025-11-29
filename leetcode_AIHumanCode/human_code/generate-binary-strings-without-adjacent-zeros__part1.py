# Time:  O(n * 2^n)
# Space: O(n)

# backtracking
class Solution(object):
    def validStrings(self, n):
        """
        """
        def backtracking(i):
            if i == n:
                result.append("".join(curr))
                return
            if not curr or curr[-1] == '1':
                curr.append('0')
                backtracking(i+1)
                curr.pop()
            curr.append('1')
            backtracking(i+1)
            curr.pop()

        result, curr = [], []
        backtracking(0)
        return result


