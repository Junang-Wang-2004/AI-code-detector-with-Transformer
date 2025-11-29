# Time:  O(n^3)
# Space: O(n)
# brute force
class Solution3(object):
    def minimizeResult(self, expression):
        """
        """
        best = None
        min_val = float("inf")
        pos = expression.index('+')
        for i in range(pos):
            for j in range(pos+1, len(expression)):
                val = (int(expression[:i] or "1")*
                       (int(expression[i:pos])+int(expression[pos+1:j+1]))*
                       int(expression[j+1:] or "1"))  # Space: O(n)
                if val < min_val:
                    min_val = val
                    best = (i, j)
        return "".join([expression[:best[0]], '(', expression[best[0]:best[1]+1], ')', expression[best[1]+1:]])  # Space: O(n)
